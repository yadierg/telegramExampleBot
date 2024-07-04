import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)


#Configure logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Soy un bot, hablame por favor'
    )


def main() -> None:
    """Run the bot."""

    # Bot's Data
    token = '1908900556:AAHiEcK2T6K0IuK04rvpjKOg3Nj6eUOAstc'
    bot = 'yayoPrueba_bot @Yayo1088Bot'
    weather_token = '19fdb2e28bf14c20b71232813240207'

    #Create Application
    
    """ application = (
        Application.builder()
        .token(token)
        .read_timeout(30)
        .write_timeout(30)
        .build()
    )
 """
    #application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    #application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    # Bot's Data
    token = '1908900556:AAHiEcK2T6K0IuK04rvpjKOg3Nj6eUOAstc'
    bot = 'yayoPrueba_bot @Yayo1088Bot'

    # Create App
    application = ApplicationBuilder().token(token).build()

    # Create Command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    #Run App
    application.run_polling()
