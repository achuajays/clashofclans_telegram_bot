import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq(api_key = os.getenv("GROQ_API_KEY"))
# Set your OpenAI API key and Telegram bot token





# OpenAI function for getting responses
async def get_openai_response(user_query):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": "Explain the query about clash of clans in the game. " + user_query,
                }
            ],
            model="llama3-8b-8192",
        )

        return chat_completion.choices[0].message.content
    except Exception as e:
        return "Sorry, I couldn't process that. Please try again later."

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your real-time clash of clan assistant. How can I help!"
    )

# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "To use this bot, simply type your question or topic, and I'll assist you!"
    )

# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text
    await update.message.reply_chat_action(action="typing")  # Indicate typing
    response = await get_openai_response(user_query)
    await update.message.reply_text(response)

# Main function to set up the bot
def main():
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
