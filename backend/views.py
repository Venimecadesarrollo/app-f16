from dotenv import load_dotenv
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.shortcuts import render
from django.core.mail import send_mail

# ? Load environment variables
load_dotenv()


# Create your views here.
def index(request):
    return render(request, "index.html")


def registro(request):
    return render(request, "registro.html")


def calculadora(request):
    return render(request, "calculadora.html")

def registro(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            
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