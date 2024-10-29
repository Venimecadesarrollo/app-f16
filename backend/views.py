import os
from dotenv import load_dotenv

from playwright.sync_api import sync_playwright, Playwright
import requests
from django.shortcuts import render
from django.http import HttpResponse

from backend.utils.requests_func import login, base_url
from backend.forms import CargoTrackForm


# ? Load environment variables
load_dotenv()


# Create your views here.
def index(request):
    return render(request, "index.html")


def registro(request):
    return render(request, "registro.html")


def calculadora(request):
    return render(request, "calculadora.html")


def make_account(playwright: Playwright, user: str, password: str, data: dict) -> None:
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    context = browser.new_context()
    # context.add_cookies(cookie_value)
    page = context.new_page()
    page.goto("https://bva.cargotrack.net/appl2.0/agent/accounts_add.asp")
    page.wait_for_timeout(1000)
    # Find an element and insert text
    page.locator("#user").fill(user)
    page.locator("#password").fill(password)
    page.locator("input[name=Submit][class=ntext-button-blue-small]").click()
    page.wait_for_timeout(2000)

    page.locator("#first_name").fill(data["first_name"])

    # other actions...
    browser.close()


def process_register(request):
    session: requests.Session = requests.Session()
    user = os.getenv("CARGOTRACK_USER")
    password = os.getenv("CARGOTRACK_PASS")
    email = os.getenv("CARGOTRACK_EMAIL")

    if request.method == "POST":
        form = CargoTrackForm(request.POST)

        if form.is_valid():
            # # ! If form is valid, send data to CargoTrack
            data = form.cleaned_data
            print(data)

            # # ? Try to login 3 times
            # max_attempts = 3
            # attempts = 0
            # login_response = None
            # cookies = None

            # while attempts < max_attempts:
            #     login_response, cookies = login(user, password, session)
            #     if login_response.status_code == 200:
            #         break
            #     attempts += 1

            # # ! If no good response, return 500 response
            # if login_response.status_code != 200:
            #     return HttpResponse("Login failed after multiple attempts")

            # ? Send data to CargoTrack
            # ? Use the same session to keep the login
            for k, v in data.items():
                if isinstance(v, bool) and v:
                    data[k] = "Y"
            data["button3"] = "Enviar"
            data["action"] = "search"
            data["consignee"] = "Y"
            data["email"] = email
            # print(session.headers)
            # creation_response = session.post("https://bva.cargotrack.net/appl2.0/agent/accounts_add.asp", data=data, allow_redirects=True)

            # Create a playwright instance to send the data
            print(data)
            with sync_playwright() as playwright:
                make_account(playwright, user=user, password=password, data=data)


            # print(creation_response.url)
            # print(creation_response.headers)
            # print(creation_response.history)
            # print(creation_response.history[0].url)
            # print(creation_response.history[0].text)
            # print(creation_response.history[0].headers)
            # print(creation_response.status_code)
            # redirect_headers = creation_response.history[0].headers
            # creation_response = 
            # print(redirect_headers)
            # print(creation_response.text)
            # print(creation_response.url)
        else:
            return HttpResponse(form.errors, status=400)

    return HttpResponse()
