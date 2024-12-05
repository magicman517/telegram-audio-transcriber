import os

from dotenv import load_dotenv
from groq import AsyncGroq

from helpers import read_audio

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL") or "whisper-large-v3-turbo"


class GroqClient:
    _instance = None

    groq_client: AsyncGroq

    def __new__(cls) -> "GroqClient":
        if not cls._instance:
            if GROQ_API_KEY is None:
                raise ValueError("Missing GROQ_API_KEY env variable")

            cls._instance = super(GroqClient, cls).__new__(cls)
            cls._instance.groq_client = AsyncGroq(api_key=GROQ_API_KEY)

        return cls._instance

    async def transcribe_audio(self, file_path) -> str:
        """
        Transcribe an audio file using whisper-large-v3-turbo model

        Params:
            file_path: path to downloaded audio

        Returns:
            str: transcription of the audio
        """

        result = await self.groq_client.audio.transcriptions.create(
            file=(os.path.basename(file_path), await read_audio(file_path)),
            model=GROQ_MODEL,
            response_format="json",
            temperature=0.5,
        )

        return result.text
