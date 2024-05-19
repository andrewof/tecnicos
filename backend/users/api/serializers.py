from rest_framework import serializers
from users.models import Cliente, Tecnico, Administrador


class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = ('cedula','name','last_name','email','direccion','codigo_postal')


class TecnicoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tecnico
    fields = ('cedula','name','last_name','email','profesion','experiencia')


class AdministradorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Administrador
    fields = ('cedula','name','last_name','email')

