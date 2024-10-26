import os
from dotenv import load_dotenv

import requests
from django.shortcuts import render
from django.http import HttpResponse

from backend.utils.requests_func import login
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


def process_register(request):
    session: requests.Session = requests.Session()
    user = os.getenv("CARGOTRACK_USER")
    password = os.getenv("CARGOTRACK_PASS")
    email = os.getenv("CARGOTRACK_EMAIL")

    if request.method == "POST":
        form = CargoTrackForm(request.POST)

        if form.is_valid():
            # ! If form is valid, send data to CargoTrack
            data = form.cleaned_data
            print(data)

            # ? Try to login 3 times
            max_attempts = 3
            attempts = 0
            login_response = None

            while attempts < max_attempts:
                login_response: requests.Response = login(user, password, session)
                if login_response.status_code == 200:
                    break
                attempts += 1

            # ! If no good response, return 500 response
            if login_response.status_code != 200:
                return HttpResponse("Login failed after multiple attempts")

            # ? Send data to CargoTrack
            # ? Use the same session to keep the login
            data["button3"] = "Enviar"
            data["action"] = "search"
            data["consignee"] = "Y"
            data["email"] = email
            creation_response = session.post("https://bva.cargotrack.net/appl2.0/agent/accounts_add.asp", data=data, allow_redirects=True)
        else:
            return HttpResponse(form.errors, status=400)

    return HttpResponse()
