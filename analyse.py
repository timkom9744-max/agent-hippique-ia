from telechargement import telecharger_page

from lecture_html import (
    extraire_hippodrome,
    extraire_discipline,
    extraire_type_trot,
    extraire_depart_trot,
    extraire_distance,
    extraire_heure,
    extraire_allocation,
    extraire_partants,
)

from url_course import extraire_reunion_course


def analyser_course(message):

    message = message.strip()

    if message.startswith("http://") or message.startswith("https://"):

        reunion, course = extraire_reunion_course(message)

        page = telecharger_page(message)

        if page:

            hippodrome = extraire_hippodrome(page)
            discipline = extraire_discipline(page)
            distance = extraire_distance(page)
            heure = extraire_heure(page)
            allocation = extraire_allocation(page)
            partants = extraire_partants(page)

            resultat = (
                "🌐 Lien détecté.\n\n"
                f"📍 Réunion : {reunion}\n"
                f"🏇 Course : {course}\n"
                f"🏟️ Hippodrome : {hippodrome}\n"
                f"🏇 Discipline : {discipline}\n"
            )

            # Informations spécifiques au trot
            if discipline == "Trot":

                type_trot = extraire_type_trot(page)

                resultat += (
                    f"🐴 Type de trot : {type_trot}\n"
                )

                if type_trot == "Attelé":

                    depart_trot = extraire_depart_trot(page)

                    resultat += (
                        f"🚦 Départ : {depart_trot}\n"
                    )

            resultat += (
                f"📏 Distance : {distance}\n"
                f"🕒 Heure : {heure}\n"
                f"💰 Allocation : {allocation}\n"
                f"🐎 Partants : {partants}\n\n"
                "✅ Analyse de la page réussie."
            )

            return resultat

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


Et voici également le code complet de la nouvelle fonction à ajouter à la fin de lecture_html.py :

python
def extraire_partants(html):

    texte = BeautifulSoup(html, "html.parser").get_text(
        separator=" ",
        strip=True
    )

    # Cas : "Partants : 16"
    resultat = re.search(
        r"Partants\s*:?\s*(\d+)",
        texte,
        re.IGNORECASE
    )

    if resultat:
        return resultat.group(1)

    # Cas : "16 Partants"
    resultat = re.search(
        r"(\d+)\s+Partants",
        texte,
        re.IGNORECASE
    )

    if resultat:
        return resultat.group(1)

    return "Inconnu"
