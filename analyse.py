from telechargement import telecharger_page
from lecture_html import extraire_hippodrome, extraire_discipline
from url_course import extraire_reunion_course


def analyser_course(message):
    message = message.strip()

    if message.startswith("http://") or message.startswith("https://"):

        reunion, course = extraire_reunion_course(message)

        page = telecharger_page(message)

        if page:

            hippodrome = extraire_hippodrome(page)
            discipline = extraire_discipline(page)

            return (
                "🌐 Lien détecté.\n\n"
                f"📍 Réunion : {reunion}\n"
                f"🏇 Course : {course}\n"
                f"🏟️ Hippodrome : {hippodrome}\n"
                f"🏇 Discipline : {discipline}\n\n"
                "✅ Analyse de la page réussie."
            )

        return "❌ Impossible de télécharger la page."

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
        "Envoie un lien de course ou une référence comme R1C4."
    )
