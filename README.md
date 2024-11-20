# Clash of Clans Telegram Assistant Bot

This is a real-time Clash of Clans assistant bot built using Python, Telegram Bot API, and Groq's AI models. The bot provides intelligent responses to user queries about Clash of Clans, leveraging the power of AI.

---

## Features

- **Real-time Assistance**: Answers user queries related to Clash of Clans.
- **Groq Integration**: Utilizes the Groq AI API for generating responses.
- **Simple Commands**: 
  - `/start`: Greet the user.
  - `/help`: Provide usage instructions.
- **Secure API Handling**: API keys are managed securely using environment variables.

---

## Prerequisites

1. **Python 3.10.12** installed.
2. **Telegram Bot Token** from [BotFather](https://core.telegram.org/bots#botfather).
3. **Groq API Key** from [Groq](https://groq.com/).
4. Required Python packages installed:
    ```bash
    pip install python-telegram-bot groq python-dotenv
    ```

---

## Setup Instructions

1. Clone this repository:
    ```bash
    git clone https://github.com/achuajays/clashofclans_telegram_bot.git
    cd clashofclans_telegram_bot
    ```

2. Create a `.env` file to store your API keys:
    ```bash
    touch .env
    ```

3. Add the following lines to the `.env` file:
    ```plaintext
    TELEGRAM_BOT_TOKEN=<your-telegram-bot-token>
    GROQ_API_KEY=<your-groq-api-key>
    ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the bot:
    ```bash
    python bot.py
    ```

---

## Project Structure

```plaintext
.
├── bot.py              # Main script for running the bot
├── .env                # Environment variables (add to .gitignore)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
