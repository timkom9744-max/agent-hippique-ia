import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐎 Bonjour ! Je suis SamTurf.\nEnvoie-moi un lien de course ou R1C4."
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.upper().strip()

    if len(message) == 4 and message.startswith("R") and "C" in message:
        await update.message.reply_text(
            f"🐎 Analyse demandée\n\nRéunion : {message[:2]}\nCourse : {message[2:]}\n\n✅ Demande enregistrée."
        )
    else:
        await update.message.reply_text(
            "Je n'ai pas compris.\nEnvoie par exemple : R1C4"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("🐎 SamTurf est en ligne...")

app.run_polling()
