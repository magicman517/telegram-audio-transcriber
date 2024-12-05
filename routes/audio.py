import logging
import os

from aiogram import F, Bot, Router
from aiogram.types import ErrorEvent, Message

from groq_client.groq_client import GroqClient
from helpers import download_audio

router = Router(name=__name__)


@router.message(F.voice)
@router.message(F.audio)
@router.message(F.video_note)
async def message_audio_handler(message: Message) -> None:
    bot = message.bot
    if not bot:
        await message.reply("Unknown error")
        return

    initial_message = await message.reply("Downloading audio...")

    file_path, file_id = await get_file_info(bot, message)
    if not file_path or not file_id:
        await initial_message.edit_text("Failed to download audio")
        return

    downloaded_file_path = await download_audio(bot, file_path, file_id)

    await initial_message.edit_text("Transcribing...")

    result = await GroqClient().transcribe_audio(downloaded_file_path)

    await initial_message.edit_text(result)

    if downloaded_file_path:
        os.remove(downloaded_file_path)


async def get_file_info(bot: Bot, message: Message) -> tuple[str | None, str | None]:
    if message.voice:
        file = await bot.get_file(message.voice.file_id)
    elif message.audio:
        file = await bot.get_file(message.audio.file_id)
    elif message.video_note:
        file = await bot.get_file(message.video_note.file_id)
    else:
        return None, None
    return file.file_path, file.file_id


@router.error()
async def error_handler(event: ErrorEvent) -> None:
    logging.error(f"Error in {__name__}: {event.exception}")

    if event.update.message:
        await event.update.message.reply("An error occurred")
