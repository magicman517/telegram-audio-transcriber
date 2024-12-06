# Telegram Audio Transcription Bot

This bot allows you to transcribe audio messages sent to a Telegram chat using the OpenAI's `whisper` model. The transcription is done using the Groq API.


---

## Requirements

Before you begin, make sure you have:

1. A Telegram bot token from [BotFather](https://t.me/BotFather).
2. A Groq API key from [GroqCloud](https://console.groq.com/keys).

---

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/magicman517/telegram-audio-transcriber.git
cd telegram-audio-transcriber
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory and add the following keys:

```env
BOT_TOKEN=your-telegram-bot-token
GROQ_API_KEY=your-groq-api-key
```

(Optional) Specify the transcription model. Default: `whisper-large-v3-turbo`. [Available models](https://console.groq.com/docs/models).

```env
GROQ_MODEL=whisper-large-v3-turbo
```

### 3. Install Dependencies

### Option A: Using a Virtual Environment

1. Create and activate a virtual environment:

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows: `.venv\Scripts\activate`
    ```

2. Install required packages:

    ```sh
    pip install -r requirements.txt
    ```

### Option B: Using Docker

1. Build the Docker image:

    ```sh
    docker build -t telegram-audio-transcriber .
    ```

---

## Running the Bot

### Option 1: Using Python

1.  Start the bot:

    ```sh
    python main.py
    ```

### Option 2: Using Docker

1.  Run the container:

    ```sh
    docker run --env-file .env telegram-audio-transcriber
    ```

2. Send an audio message, voice message, or video note to the bot.

3. The bot will transcribe the audio and reply with the transcription.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.