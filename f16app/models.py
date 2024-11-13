from django.db import models

class UserProfile(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.TextField()
    codigo_postal = models.CharField(max_length=10)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

