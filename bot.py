import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me a file hosting link to process.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Send a supported file hosting URL (e.g., DoodStream, Streamtape).')

def handle_message(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    update.message.reply_text(f"Processing: {url}")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
