from django.contrib import admin
from .models import User, Cliente, Tecnico, Administrador

# Register your models here.
admin.site.register(User)
admin.site.register(Cliente)
admin.site.register(Tecnico)
admin.site.register(Administrador)