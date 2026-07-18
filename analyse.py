def analyser_course(message):
    message = message.strip()

    if message.startswith("http://") or message.startswith("https://"):
        return (
            "🌐 Lien détecté.\n\n"
            "🔎 Préparation de l'analyse de la course..."
        )

    message = message.upper()

    if "C" in message:
        parties = message.split("C")

        if len(parties) == 2:
            reunion = parties[0]
            course = "C" + parties[1]

            return (
                "🐎 Analyse demandée\n\n"
                f"📍 Réunion : {reunion}\n"
                f"🏇 Course : {course}\n\n"
                "✅ Demande enregistrée.\n"
                "🔎 Préparation de l'analyse..."
            )

    return (
        "❌ Je n'ai pas compris.\n\n"
        "Envoie par exemple :\n"
        "R1C4\n\n"
        "ou un lien vers une course."
    )
