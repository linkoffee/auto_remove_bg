"""Bot function tests."""
import pytest
from unittest.mock import patch, AsyncMock, MagicMock

import main


@pytest.mark.asyncio
async def test_on_ready():
    """Checks on_ready event."""
    # Mock the bot object and its user property
    mock_bot = MagicMock()
    mock_bot.user.name = 'test_bot'
    mock_bot.user.id = 1234567890

    # Patch the logger to mock its behavior
    with patch.object(main.logger, 'info') as mock_log:
        # Patch the bot to return our mock_bot
        with patch('main.bot', mock_bot):
            await main.on_ready()
            mock_log.assert_called_with(
                f'Logged in as {mock_bot.user.name} ({mock_bot.user.id})'
            )


@pytest.mark.asyncio
async def test_on_message(bot, msg):
    """Checks on_message event."""
    with patch('main.is_supported_file', return_value=False):
        with patch('main.handle_remove_bg') as mock_handle:
            await main.on_message(msg)
            mock_handle.assert_not_called()

    msg.attachments = [MagicMock()]
    with patch('main.is_supported_file', return_value=True):
        with patch('main.handle_remove_bg') as mock_handle:
            await main.on_message(msg)
            mock_handle.assert_called_once()


@pytest.mark.asyncio
async def test_handle_remove_bg(ctx, attachment):
    """Checks that the image is being processed."""
    ctx.send = AsyncMock()

    with patch('main.download_file', return_value='test_path.png'):
        with patch('main.remove_background',
                   return_value=[{'slug': 'no-bg', 'path': 'test_path'}]):
            with patch('os.remove') as mock_remove:
                await main.handle_remove_bg(ctx, attachment)
                ctx.send.assert_any_call(
                    main.MESSAGES[main.LANGUAGE]['PRE_REMOVE_MSG']
                )
                ctx.send.assert_any_call(
                    main.MESSAGES[main.LANGUAGE]['WAITING_MSG']
                )
                ctx.send.assert_any_call(
                    main.MESSAGES[main.LANGUAGE]['RESULT_MSG']
                )
                mock_remove.assert_called_once_with('test_path.png')


@pytest.mark.asyncio
async def test_set_language(ctx):
    """Checks the ability to change localization."""
    await main.set_language(ctx, 'en')
    ctx.send.assert_called_with('Language set to en.')

    await main.set_language(ctx, 'unsupported_lang')
    ctx.send.assert_called_with('Language unsupported_lang is not supported.')


@pytest.mark.asyncio
async def test_bot_info(ctx):
    """Checks the ability to get information about the bot."""
    await main.bot_info(ctx)
    ctx.send.assert_called_with(
        main.MESSAGES[main.LANGUAGE]['INFO_MSG']
    )
