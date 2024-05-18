from django.db import models
from users.models import Cliente, Tecnico


class Services(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_visita = models.DateField(auto_now_add=False)
    hora_solicitud = models.TimeField(auto_now_add=True)
    hora_visita = models.TimeField(auto_now_add=False)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descripcion} {self.fecha_solicitud} {self.fecha_visita} {self.hora_solicitud} {self.hora_visita}'
    
