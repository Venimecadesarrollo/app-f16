import requests
from bs4 import BeautifulSoup
from typing import Any, Dict, List



base_url = "https://bva.cargotrack.net/default.asp"


def login(user: str, password: str, session: requests.Session) -> None:
    data = {"user": user, "password": password, "Submit": "Log In", "action": "login"}
    session.post(
        url=base_url, data=data, headers=headers, allow_redirects=True
    )

if __name__ == "__main__":
    session = requests.Session()

    # Configuramos las cabeceras iniciales
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Origin": "https://bva.cargotrack.net",
        "Access-Control-Allow-Origin": "*",
    }
    session.headers.update(headers)

    # Hacemos la solicitud inicial para obtener las cookies
    home_response = session.get(base_url)
    cookie_value = f"user={user};{home_response.headers['Set-Cookie']}"
    session.headers.update({"cookie": cookie_value})

    # Iniciamos sesión
    login(user, password, session)
    print("Logged IN.")