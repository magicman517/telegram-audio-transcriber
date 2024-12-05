import os

import aiofiles
from aiogram import Bot


async def download_audio(bot: Bot, file_path: str, file_id: str) -> str:
    """
    Download audio from telegram

    Params:
        bot: Bot - bot instance
        file_path: str - file path
        file_id: str - file id

    Returns:
        str - downloaded file path
    """

    if not os.path.exists("audios"):
        os.makedirs("audios")

    await bot.download_file(file_path, f"audios/{file_id}.mp3")

    return f"audios/{file_id}.mp3"


async def read_audio(file_path: str) -> bytes:
    """
    Read downloaded audio

    Params:
        file_path: str - file path

    Returns:
        bytes - audio bytes
    """

    async with aiofiles.open(file_path, "rb") as file:
        return await file.read()
