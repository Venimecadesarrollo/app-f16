from dotenv import load_dotenv
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# ? Load environment variables
load_dotenv()


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Captura los datos del formulario de contacto
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            # Construcción del mensaje de correo
            subject = f'Nuevo mensaje de contacto: {asunto}'
            message = (
                f'Nombre: {nombre}\n'
                f'Correo electrónico: {email}\n'
                f'Mensaje:\n{mensaje}\n'
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['contacto@f16cargo.com']  # Correo de destino

            # Envío del correo
            send_mail(subject, message, from_email, recipient_list)

            # Redirige a la página de confirmación
            return redirect('msj_contacto')  # Asegúrate de que 'mensaje_enviado' esté en tu archivo urls.py

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


# def registro(request):
#     return render(request, "registro.html")


def calculadora(request):
    return render(request, "calculadora.html")


def registro(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():

            user_profile = form.save()
            user_profile.email = user_profile.correo
            # Generate a username with form data
            user_profile.username = f"{user_profile.nombre.lower()}.{user_profile.apellido.lower()}"
            user_profile.save()
            # Datos para enviar por correo
            subject = 'Nuevo Registro de Usuario'
            message = (
                f'Nombre: {user_profile.nombre}\n'
                f'Apellido: {user_profile.apellido}\n'
                f'País: {user_profile.pais}\n'
                f'Estado: {user_profile.estado}\n'
                f'Ciudad: {user_profile.ciudad}\n'
                f'Dirección: {user_profile.direccion}\n'
                f'Código Postal: {user_profile.codigo_postal}\n'
                f'Correo: {user_profile.correo}\n'
                f'Teléfono: {user_profile.telefono}\n'
            )
            from_email = 'administracion@f16cargo.com'
            recipient_list = ['administracion@f16cargo.com']  # Cambia por el correo al que quieras enviar
            
            # Enviar correo
            send_mail(subject, message, from_email, recipient_list)

            return redirect('registro_creado')  # Cambia por la URL de tu página principal
    else:
        form = UserProfileForm()
    
    return render(request, 'registro.html', {'form': form})

def registro_creado(request):
    return render(request, "registro_creado.html")

def msj_contacto(request):
    return render(request, 'msj_contacto.html')

def msj_login(request):
    return render(request, "msj_login.html")
