from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def _create_user(self, email, username, name, last_name, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email debe ser provisto')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            name=name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using= self.db)
        return user
    
    def create_user(self, email, username, last_name, password=None, **extra_fields):
        return self._create_user(email, username, last_name, password, False, False, **extra_fields)
    
    def create_superuser(self, email, username, last_name, password=None, **extra_fields):
        return self._create_user(email, username, last_name, password, True, True, **extra_fields)
        
        

class User(AbstractBaseUser, PermissionsMixin):
    cedula = models.CharField(unique=True, max_length=40, blank=False, null=False)
    email = models.EmailField('Correo Electrónico', unique=True, blank=False, null=False)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    name = models.CharField('Nombres', max_length=200, blank=False, null=False)
    last_name = models.CharField('Apellidos', max_length=200, blank=False, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    historical = HistoricalRecords()
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['cedula', 'name', 'last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Cliente(User):
    direccion = models.CharField(max_length=100, blank=True)
    codigo_postal = models.CharField(max_length=20, blank=True)


class Tecnico(User):
    profesion = models.CharField(max_length=100)
    experiencia = models.IntegerField()

class Administrador(User):
    pass

class HistoricalUser(models.Model):
    id = models.AutoField(primary_key= True)