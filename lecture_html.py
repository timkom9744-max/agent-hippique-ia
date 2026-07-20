from bs4 import BeautifulSoup


def lire_titre(html):
    soup = BeautifulSoup(html, "html.parser")

    if soup.title:
        return soup.title.text.strip()

    return ""


def extraire_hippodrome(html):

    titre = lire_titre(html)

    if not titre:
        return "Inconnu"

    parties = titre.split(" - ")

    if len(parties) >= 2:
        return parties[1].strip()

    return "Inconnu"


def extraire_discipline(html):

    texte = BeautifulSoup(html, "html.parser").get_text(
        separator=" ",
        strip=True
    )

    texte = texte.lower()

    if "trot" in texte:
        return "Trot"

    if "haies" in texte:
        return "Haies"

    if "steeple" in texte:
        return "Steeple-Chase"

    if "cross" in texte:
        return "Cross"

    if "monté" in texte or "monte" in texte:
        return "Monté"

    if "plat" in texte:
        return "Plat"

    return "Inconnue"
