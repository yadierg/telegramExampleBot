from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text( "Hola Mundo" )


def main() -> None:
    """Run the bot."""

    # Bot's Data
    token = '1908900556:AAHiEcK2T6K0IuK04rvpjKOg3Nj6eUOAstc'
    bot = 'yayoPrueba_bot @Yayo1088Bot'

    #Create Application
    application = (
        Application.builder()
        .token(token)
        .read_timeout(30)
        .write_timeout(30)
        .build()
    )

    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
