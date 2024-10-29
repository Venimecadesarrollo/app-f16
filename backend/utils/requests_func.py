import requests
from typing import Any, Dict, List


base_url = "https://bva.cargotrack.net/default.asp"


def set_headers(session: requests.Session) -> None:
    """Configures headers for session.

    Parameters
    ----------
    session : requests.Session
        Session object.
    """
    # Configuramos las cabeceras iniciales
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        "Origin": "https://bva.cargotrack.net",
        "Access-Control-Allow-Origin": "*",
    }
    session.headers.update(headers)


def login(user: str, password: str, session: requests.Session) -> requests.Response:
    """Perfom login on BVA website.

    Parameters
    ----------
    user : str
        User name.
    password : str
        Account Password.
    session : requests.Session
        Session object

    Returns
    -------
    requests.Response
        Login response.
    """

    set_headers(session)

    # ? Hacemos la solicitud inicial para obtener las cookies
    home_response = session.get(base_url)
    cookie_value = f"user={user};{home_response.headers['Set-Cookie']}"
    session.headers.update({"cookie": cookie_value})

    # ? Iniciamos sesión
    data = {"user": user, "password": password, "Submit": "Log In", "action": "login"}
    login_response = session.post(url=base_url, data=data, allow_redirects=True)
    return login_response
