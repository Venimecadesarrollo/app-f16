from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class UserProfile(AbstractUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.TextField()
    codigo_postal = models.CharField(max_length=10)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Field for storing hashed passwords

    def save(self, *args, **kwargs):
        # Ensure the password is hashed before saving
        if not self.password.startswith('pbkdf2_sha256$'):  # Check if password is already hashed
            self.password = make_password(self.password)
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
