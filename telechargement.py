import requests


def telecharger_page(url):
    try:
        reponse = requests.get(url, timeout=10)

        if reponse.status_code == 200:
            return reponse.text

        return None

    except Exception:
        return None
