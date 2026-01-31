from cmath import log
from config import Config
import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Disable telegram HTTP POST to /getUpdates
logging.getLogger("httpx").setLevel(logging.WARNING)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.effective_message is not None
    await update.effective_message.reply_text("Hello world")


def main():
    logger.info("building app...")
    app = Application.builder().token(Config.TELEGRAM_BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.ALL, hello))

    logger.info("Starting bot...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    print("hola")
    main()
