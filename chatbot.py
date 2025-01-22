import json
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Load the chat history from the JSON file
with open("chat_history.json", "r", encoding="utf-8") as file:
    chat_history = json.load(file)["messages"]

# Function to find the appropriate reply
def find_reply(input_text):
    input_words = set(input_text.strip().split())
    match_candidates = []

    # Step 1: Collect messages with their number of common words
    for message in chat_history:
        if "text" in message and isinstance(message["text"], str):
            message_words = set(message["text"].strip().split())
            common_word_count = len(input_words & message_words)
            if common_word_count > 2 :# Only consider messages with more than 2 words in common
                print(message_words)
                match_candidates.append((common_word_count, message["id"]))

    # Step 2: Prioritize messages by common word count
    match_candidates.sort(reverse=True, key=lambda x: x[0])  # Sort by common_word_count (descending)

    # Step 3: Try to find a reply starting with the highest priority
    for _, matched_id in match_candidates:
        for message in chat_history:
            if message.get("reply_to_message_id") == matched_id:
                return message.get("text")

    return None  # No reply found for any match

# Telegram message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    bot_response = find_reply(user_message)

    if bot_response:
        await update.message.reply_text(bot_response)
    # Else: Say nothing (no response)

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your chat bot. Type something to see what I reply!")

# Main function
def main():
    # Replace 'YOUR_BOT_TOKEN' with your bot token from @BotFather
    application = ApplicationBuilder().token("7876541643:AAETxa5cAIkv6fK94hEYVfWxedE1iaH_dXg").build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
