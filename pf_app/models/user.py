from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('Users must have an username')
        elif not password:
            raise ValueError('Users must have a password')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password):

        user = self.create_user(username=username, password=password,)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    #papasFersanuser no tiene id
    #usuario_id = models.CharField(primary_key=True)
    #username de ppasfersan es email
    id_usuario = models.BigAutoField('id_usuario',primary_key=True)
    username = models.CharField('username',max_length=30, unique=True ,default='loser')
    password = models.CharField('password',max_length=300)
    apellido = models.CharField('apellido',max_length=30,default='apellido')
    nombre = models.CharField('nombre',max_length=30,default='nombre')
    email = models.EmailField('correo',max_length=100,default='nombre@dominio.com')
    direccion = models.CharField('direccion',max_length=50,default='calle 1 carrera 1 # 1')
    telefono = models.CharField('telefono',max_length=15,default='00000000')
    estado = models.BooleanField('activo',default=True)

    def save(self, **kwargs):
        some_salt = '5tgT5678Ikju89IKj'
        self.password = make_password(self.password, some_salt)
        AbstractBaseUser.save(**kwargs)
        #super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username'