import re


def extraire_reunion_course(url):

    resultat = re.search(r"(R\d+)C(\d+)", url.upper())

    if resultat:

        reunion = resultat.group(1)
        course = "C" + resultat.group(2)

        return reunion, course

    return None, None
