from telechargement import telecharger_page
from lecture_html import lire_infos
from url_course import extraire_reunion_course


def analyser_course(message):
    message = message.strip()

    if message.startswith("http://") or message.startswith("https://"):

        reunion, course = extraire_reunion_course(message)

        page = telecharger_page(message)

        if page:

            infos = lire_infos(page)

            texte = "\n".join(infos)

            return (
                "🌐 Lien détecté.\n\n"
                f"📍 Réunion : {reunion}\n"
                f"🏇 Course : {course}\n\n"
                "✅ Analyse de la page réussie.\n\n"
                "📋 Éléments détectés :\n\n"
                f"{texte}"
            )

        return "❌ Impossible de télécharger la page."

    message = message.upper()

    reunion, course = extraire_reunion_course(message)

    if reunion and course:

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
