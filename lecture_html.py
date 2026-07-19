from bs4 import BeautifulSoup


def lire_titre(html):
    soup = BeautifulSoup(html, "html.parser")

    if soup.title:
        return soup.title.text.strip()

    return "Titre introuvable"
