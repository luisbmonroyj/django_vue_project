### Ya es funcional

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
#hashers codes password to save it in the DB

class UserManager(BaseUserManager):
    def create_user(self,username,password=None):
        if not username:
            raise ValueError ('Debe escribir un nombre de usuario')
            #username must not be empty
        elif not password:
            raise ValueError ('Debe escribir una contraseña')
            #password too
        
        user = self.model(username=username)
        #creates a user with a username
        user.set_password(password)
        #sets the password for user
        user.save(using=self._db)
        #I DONT KNOW WHY IT IS SELF._DB
        return user

    def create_superuser(self,username,password):
        superuser = self.create_user(username=username,password=password,)
        #calls self method and changes superuser attribute to true
        superuser.is_admin = True
        superuser.save(using=self._db)
        return superuser

#esta es la clase que crea el usuario como un objeto
class User(AbstractBaseUser, PermissionsMixin):
    #General structure for a model 
    # object = DBdatatype('ColumnName',properties)
    id_usuario = models.BigAutoField('id_usuario',primary_key=True)
    username = models.CharField('usuario',max_length=30, unique=True ,default='loser')
    password = models.CharField('password',max_length=300)
    apellido = models.CharField('apellido',max_length=30,default='apellido')
    nombre = models.CharField('nombre',max_length=30,default='nombre')
    email = models.EmailField('correo',max_length=100,default='nombre@dominio.com')
    direccion = models.CharField('direccion',max_length=50,default='calle 1 carrera 1 # 1')
    telefono = models.CharField('telefono',max_length=15,default='00000000')
    estado = models.BooleanField('activo',default=True)
    #The JSON must have at least the password, the rest are created with the default
    def save(self, **kwargs):
        self.password = make_password(self.password)
        super().save(**kwargs)
    #WHERE objects DID COME FROM AND WHAT IS IT FOR
    objects = UserManager()
    #USERNAME_FIELD MUST HAVE THE object that stores the username, Ln 35
    USERNAME_FIELD = 'username'
    
