"""This module contains a Discord bot logic."""
import os
import logging
import logging.config
import tempfile
from http import HTTPStatus

import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv

from localization import MESSAGES

load_dotenv()

# Tokens:
BOT_TOKEN = os.getenv('BOT_TOKEN')
BALA_TOKEN = os.getenv('BALA_TOKEN')

# Endpoints:
ENDPOINT = 'https://api.ba-la.ru/api/remove'

# Base language:
LANGUAGE = 'en'  # 'en', 'ru', 'es', 'zh', 'ar'

# Logging configuration
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Ensure message content intent is enabled

bot = commands.Bot(command_prefix='/', intents=intents)


def is_supported_file(file_name):
    """Check if the file format is supported."""
    return file_name.endswith(('.png', '.jpg', '.bmp'))


def remove_background(file_path):
    """Send the image to the API to remove the background."""
    try:
        with open(file_path, 'rb') as file:
            response = requests.post(
                ENDPOINT,
                files={'mediaFile': file},
                headers={'api-key': BALA_TOKEN},
            )
        logger.debug(
            f'API response status code: {response.status_code}'
        )
        if response.status_code != HTTPStatus.OK:
            logger.error(
                f'Connection failed. Status code: {response.status_code}'
            )
            return None

        return response.json()
    except Exception as e:
        logger.error(f'Exception during background removal: {e}')
        return None


async def download_file(attachment):
    """Download the attached file."""
    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(attachment.filename)[1]
    )
    file_path = temp_file.name
    try:
        await attachment.save(file_path)
        logger.debug(f'File has been downloaded to {file_path}')
        return file_path
    except Exception as e:
        logger.error(f'Exception during file download: {e}')
        return None
    finally:
        temp_file.close()


async def handle_remove_bg(ctx, attachment):
    """Handle the remove background process."""
    file_name = attachment.filename.lower()

    if not is_supported_file(file_name):
        await ctx.send(
            "Unsupported file format. Please upload a PNG, JPG, or BMP file."
        )
        logger.warning(f'Unsupported file format: {file_name}')
        return

    file_path = await download_file(attachment)
    if not file_path:
        await ctx.send("Failed to download the image. Please try again later.")
        return

    result = remove_background(file_path)

    await ctx.send(MESSAGES[LANGUAGE]['PRE_REMOVE_MSG'])

    if not result:
        await ctx.send("Failed to process the image. Please try again later.")
        return

    await ctx.send(MESSAGES[LANGUAGE]['WAITING_MSG'])

    no_bg_url = next((item['path']
                     for item in result if item['slug'] == 'no-bg'), None)

    if no_bg_url:
        await ctx.send(MESSAGES[LANGUAGE]['RESULT_MSG'])
        await send_image(ctx, no_bg_url, file_name)
        logger.info(f'Background removed for file `{file_name}`')
    else:
        await ctx.send(
            "Failed to retrieve the processed image. Please try again later."
        )
        logger.error(
            f'Failed to retrieve processed image for file `{file_name}`'
        )
    os.remove(file_path)
    logger.debug(f'Temporary file {file_path} has been deleted')
    await ctx.send(MESSAGES[LANGUAGE]['AGAIN?_MSG'])


async def send_image(ctx, url, original_file_name):
    """Download the processed image and send it to the user."""
    try:
        response = requests.get(url)
        if response.status_code == HTTPStatus.OK:
            temp_file = tempfile.NamedTemporaryFile(
                delete=False, suffix='.png')
            temp_file.write(response.content)
            temp_file.close()
            await ctx.send(
                file=discord.File(
                    temp_file.name,
                    filename=f"auto_remove_bg_{original_file_name}"
                )
            )
            os.remove(temp_file.name)
            logger.debug(
                f'Sent processed image and deleted temporary file {temp_file.name}')
        else:
            await ctx.send("Failed to download the processed image. Please try again later.")
            logger.error(f"Failed to download the processed image from {url}")
    except Exception as e:
        await ctx.send("An error occurred while downloading the processed image. Please try again later.")
        logger.error(f"Exception during downloading the processed image: {e}")


@bot.event
async def on_ready():
    """Logging successful connection to the bot."""
    logger.info(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.event
async def on_message(message):
    """Event handler for receiving messages."""
    logger.info(f'Received message: {message.content} from {message.author}')
    if message.author == bot.user:
        return

    # Process attached images
    if message.attachments:
        for attachment in message.attachments:
            if is_supported_file(attachment.filename.lower()):
                await handle_remove_bg(message.channel, attachment)
                return

    await bot.process_commands(message)


@bot.event
async def on_guild_join(guild):
    """Sending a start message."""
    welcome_channel = None
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            welcome_channel = channel
            break

    if welcome_channel:
        await welcome_channel.send(MESSAGES[LANGUAGE]['START_MSG'])
        logger.info(f'Sent start message to {guild.name}')
    else:
        logger.warning(
            'No suitable channel found to '
            f'send start message in {guild.name}'
        )


@bot.command()
async def set_language(ctx, lang):
    """Command to change the current localization."""
    global LANGUAGE
    if lang in MESSAGES:
        LANGUAGE = lang
        await ctx.send(f'Language set to {lang}.')
        logger.info(f'Language set to {lang}')
    else:
        await ctx.send(f'Language {lang} is not supported.')
        logger.warning(f'Tried to set unsupported language: {lang}')


@bot.command()
async def bot_info(ctx):
    """Command to show bot info."""
    await ctx.send(MESSAGES[LANGUAGE]['INFO_MSG'])

if BOT_TOKEN:
    try:
        bot.run(BOT_TOKEN)
    except Exception as e:
        logger.error(f"Error running bot: {e}")
else:
    logger.error(
        "BOT_TOKEN is not set. Please set the BOT_TOKEN environment variable.")
