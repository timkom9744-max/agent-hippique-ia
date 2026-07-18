import os
import re

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐎 Bonjour ! Je suis SamTurf.\n\n"
        "Je suis prêt à analyser les courses hippiques.\n\n"
        "Exemple : R1C4"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.upper().strip()

    if re.fullmatch(r"R\d+C\d+", message):
        parties = message.split("C")
        reunion = parties[0]
        course = "C" + parties[1]

        await update.message.reply_text(
            "🐎 Analyse demandée\n\n"
            f"📍 Réunion : {reunion}\n"
            f"🏇 Course : {course}\n\n"
            "✅ Demande enregistrée.\n"
            "🔎 Préparation de l'analyse..."
        )
    else:
        await update.message.reply_text(
            "❌ Je n'ai pas compris.\n\n"
            "Exemple attendu : R1C4"
        )


def main():
    if not TOKEN:
        print("❌ Erreur : token Telegram absent dans .env")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    )

    print("🐎 SamTurf v0.3 est en ligne...")

    app.run_polling()


if _name_ == "_main_":
    main()
