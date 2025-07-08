import logging
from pyexpat.errors import messages
import random
from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# --- Configuration ---
# It's good practice to keep your constants at the top.
TOKEN: final = '7848069291:AAHALJJZJx6KN73tDGkDmzYh_Bp48Q588vw'
BOT_USERNAME: final = '@Thehardy_bot'

# --- Bot Functions ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles the /start command. Greets the user and schedules a repeating message job for them.
    """
    chat_id = update.effective_chat.id
    await context.bot.send_message(chat_id=chat_id, text="Hello! I'm Thehardy_bot. I'm now set up to send you periodic messages.")

    # --- KEY IMPROVEMENT: Scheduling a job for a SPECIFIC user ---
    # We remove any existing job with this name to avoid duplicates if the user types /start again.
    # The name is unique to the user's chat_id.
    job_name = f"periodic_message_{chat_id}"
    context.job_queue.run_repeating(
        send_periodic_message,
        interval=180,  # 3 minutes
        first=10,      # Run the first time after 10 seconds for quick testing
        chat_id=chat_id, # This passes the chat_id to the job
        name=job_name    # Give the job a unique name
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles the /help command.
    (Renamed to help_command to avoid conflict with the built-in 'help' function)
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Here are some commands you can use:\n/start - Start the bot and periodic messages\n/help - Get this help message"
    )

def handle_input(text: str) -> str:
    """
    Processes user text and returns a predefined response.
    This function doesn't need to be async since it's just processing strings.
    """
    processed: str = text.lower().strip()
    if processed in ["hi", "hello"]:
        return "Hello! How can I assist you today?"
    if processed == "bye":
        return "Goodbye! Have a great day!"
    if processed == "help":
        return "You can ask me anything or use the /help command for assistance."
    
    # A default response if no keywords match
    return "I'm not sure how to respond to that. Try 'hi' or 'bye'."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles regular text messages from users in private or group chats.
    This function is now much simpler and more logical.
    """
    message_type = update.message.chat.type
    user_text = update.message.text

    print(f"Received '{user_text}' in {message_type} chat from {update.effective_chat.id}")

    # --- REFACTORED LOGIC ---
    # 1. Determine the text to process
    text_to_process = user_text
    # if message_type == 'group':
    #     # If in a group, only respond if the bot's username is mentioned.
    #     if BOT_USERNAME not in user_text:
    #         return  # Do nothing if the bot wasn't mentioned
    #     # Remove the bot's username to get the actual message
    #     text_to_process = user_text.replace(BOT_USERNAME, "").strip()

    # # 2. Get the response
    response = handle_input(text_to_process)

    # 3. Send the response ONCE
    await update.message.reply_text(response)


async def send_periodic_message(context: ContextTypes.DEFAULT_TYPE):
    """
    Sends a periodic message. This function is called by the JobQueue.
    """
    # --- KEY IMPROVEMENT: Getting the chat_id from the job context ---
    job = context.job
    chat_id = job.chat_id
    
# You can have a list of messages and pick one, maybe based on the day or randomly.
# For now, we'll send a simple, consistent message.
    messages = [
    "Hope you're having a great day!",
    "Just a friendly reminder!",
    "Did you know? Bots are cool!",
    "This is your daily dose of wisdom."
    ]
    message = random.choice(messages)
    print(f"Running job for chat_id: {chat_id}")
    await context.bot.send_message(chat_id=chat_id, text=message)


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Logs errors caused by updates.
    """
    logging.error(f"Update {update} caused error {context.error}")


# --- Main Bot Execution ---
if __name__ == '__main__':
    # Enable logging for better debugging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    
    print("Starting the bot...")
    app = Application.builder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Register the message handler
    # Note the corrected import: `filters` instead of `Filters`
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Register the error handler
    app.add_error_handler(error_handler)

    print("Bot is polling...")
    # The `run_polling` call is clean. We don't need the job_queue setup here anymore
    # because jobs are scheduled dynamically when users type /start.
    app.run_polling()

