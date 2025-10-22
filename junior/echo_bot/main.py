# Junior: echo_bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "1791268544:AAHxxC--WeQSYef-x30hmaUkNhRl5lMES-o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum Man Echo botman.Lyuboy matni qaytaraman")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text:
        await update.message.reply_text(update.message.text)
        return

    if update.message.photo:
        await update.message.reply_text("Rasm oldim lekin man faqat matnni takrorlayma")
        return

    await update.message.reply_text("Bu turdagi xabarni hozircha qaytara olmayman")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & (~filters.COMMAND), echo))

    print("Bot ishga tushmoqda...")
    app.run_polling()

if __name__ == "__main__":
    main()
