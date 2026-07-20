import re

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


def extraire_distance(html):

    texte = BeautifulSoup(html, "html.parser").get_text(
        separator=" ",
        strip=True
    )

    resultat = re.search(
        r"\b\d{3,4}\s?m\b",
        texte,
        re.IGNORECASE
    )

    if resultat:
        return resultat.group()

    return "Inconnue"


def extraire_heure(html):

    texte = BeautifulSoup(html, "html.parser").get_text(
        separator=" ",
        strip=True
    )

    resultat = re.search(
        r"\b\d{1,2}:\d{2}\b",
        texte
    )

    if resultat:
        return resultat.group()

    return "Inconnue"


def extraire_allocation(html):

    texte = BeautifulSoup(html, "html.parser").get_text(
        separator=" ",
        strip=True
    )

    # Recherche prioritaire : "Allocation : 25 000 €"
    resultat = re.search(
        r"Allocation\s*:?\s*([\d\s]+€)",
        texte,
        re.IGNORECASE
    )

    if resultat:
        return resultat.group(1).strip()

    # Recherche de secours : premier montant en euros
    resultat = re.search(
        r"(\d[\d\s]*\d)\s*€",
        texte
    )

    if resultat:
        return resultat.group().strip()

    return "Inconnue"
