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
