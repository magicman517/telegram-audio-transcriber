# Telegram Audio Transcription Bot

This bot allows you to transcribe audio messages sent to a Telegram chat using the OpenAI's `whisper` model. The transcription is done using the Groq API.

## Prerequisites

- Telegram bot token from [BotFather](https://t.me/BotFather)
- Groq API key from [GroqCloud](https://console.groq.com/keys)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/magicman517/telegram-audio-transcriber.git
    cd telegram-audio-transcriber
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your bot token and Groq API key:

    ```env
    BOT_TOKEN=your-telegram-bot-token
    GROQ_API_KEY=your-groq-api-key
    ```

    Optionally, you can also specify the model to use for transcription. You can find a list of available models [here](https://console.groq.com/docs/models). Default is `whisper-large-v3-turbo`.

    ```env
    GROQ_MODEL=whisper-large-v3-turbo
    ```

## Usage

1. Run the bot:

    ```sh
    python main.py
    ```

2. Send an audio message, voice message, or video note to your bot.

3. The bot will download the audio, transcribe it using the Groq API, and reply with the transcription.