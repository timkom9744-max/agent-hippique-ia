from bs4 import BeautifulSoup


def lire_infos(html):
    soup = BeautifulSoup(html, "html.parser")

    texte = soup.get_text(separator=" ", strip=True)

    mots = [
        "R1",
        "C1",
        "C2",
        "C3",
        "C4",
        "C5",
        "C6",
        "C7",
        "C8",
        "Prix",
        "Départ",
        "Partants",
    ]

    trouves = []

    for mot in mots:
        if mot in texte:
            trouves.append(mot)

    return trouves
