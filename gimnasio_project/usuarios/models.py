from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    horario = models.DateTimeField()
    cupos_disponibles = models.IntegerField(default=0)  # Establecer valor por defecto

    def __str__(self):
        return self.nombre

class Reserva(models.Model):    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'clase') 
    def __str__(self):
        return f"Reserva de {self.usuario.username} para {self.clase.nombre}"
