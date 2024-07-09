"""Fixtures for bot tests."""
import sys
import os
import pytest
from discord.ext import commands
import discord
from unittest.mock import AsyncMock, MagicMock

# Path configuration:
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


@pytest.fixture
def bot():
    """Creates and returns a bot object."""
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix='/', intents=intents)
    return bot


@pytest.fixture
def ctx(bot):
    """Creates and returns a command context."""
    ctx = MagicMock()
    ctx.bot = bot
    ctx.send = AsyncMock()
    return ctx


@pytest.fixture
def msg():
    """Creates and returns a message object."""
    msg = MagicMock(spec=discord.Message)
    msg.content = 'hello!'
    msg.author = MagicMock(spec=discord.User)
    msg.attachments = []
    return msg


@pytest.fixture
def attachment():
    """Creates and returns an attachment object."""
    attachment = MagicMock(spec=discord.Attachment)
    attachment.filename = 'image.png'
    attachment.save = AsyncMock()
    return attachment
