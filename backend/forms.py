from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nombre', 'apellido', 'pais', 'estado', 'ciudad', 'direccion', 'codigo_postal', 'correo', 'telefono']


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    asunto = forms.CharField(max_length=100, required=True)
    mensaje = forms.CharField(widget=forms.Textarea, required=True)
