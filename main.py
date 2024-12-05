import asyncio
import logging

from bot import run_bot
from groq_client.groq_client import GroqClient


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    GroqClient()  # create an instance just to check if api key is in env

    asyncio.run(run_bot())
