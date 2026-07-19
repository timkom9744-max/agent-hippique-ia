from telechargement import telecharger_page
from lecture_html import lire_infos


def analyser_course(message):
    message = message.strip()

    if message.startswith("http://") or message.startswith("https://"):

        page = telecharger_page(message)

        if page:

            infos = lire_infos(page)

            if infos:
                texte = "\n".join(infos)

                return (
                    "🌐 Lien détecté.\n\n"
                    "✅ Analyse de la page réussie.\n\n"
                    "📋 Éléments détectés :\n\n"
                    f"{texte}"
                )

            return (
                "⚠️ La page a été téléchargée mais aucun élément attendu n'a été trouvé."
            )

        return "❌ Impossible de télécharger la page."

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
