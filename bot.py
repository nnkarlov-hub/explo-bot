import random
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def explo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    value = random.randint(0, 100)
    await update.message.reply_text(f"🔥 эксплозивность: {value}%")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("explo", explo))
app.run_polling()
