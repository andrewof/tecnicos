from django.contrib import admin
from .models import Cliente, Tecnico, Administrador

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Administrador)