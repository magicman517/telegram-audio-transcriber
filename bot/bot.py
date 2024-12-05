import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from routes import audio_router

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot: Bot


async def run_bot() -> None:
    if BOT_TOKEN is None:
        raise ValueError("Missing BOT_TOKEN env variable")

    global bot
    bot = Bot(BOT_TOKEN)

    dp = Dispatcher()
    dp.include_routers(audio_router)

    await dp.start_polling(bot)
