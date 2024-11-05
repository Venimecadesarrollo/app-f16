from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nombre', 'apellido', 'pais', 'estado', 'ciudad', 'direccion', 'codigo_postal', 'correo', 'telefono']

