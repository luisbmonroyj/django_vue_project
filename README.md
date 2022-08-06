**Instalar requerimientos del proyecto.**

la idea es para no tener que ignorar varios ambientes virtuales de trabajo en el archivo .gitignore, se use el nombre ambiente_1 como ambiente virtual.

Inicialmente, ejecuta en tu maquina el comando python -m venv ambiente_1

para activar el ambiente_1 con un alias (amb), use esta instruccion en la terminal:
    doskey amb="ambiente_1\Scripts\activate"

ya solo se necesita escribir amb, para activar el ambiente

 y luego ejecuta el siguente comando:    
```
    pip install -r packages.txt
```

luego de instalado, ignorar este archivo para el desplieGe de la aplicacion

**Forma de probar con el shell**

python manage.py shell
import django 
django.setup()
from pf_app.models.Modelo import Clases
para importar los modelos que se van a probar
Modelo.objects.all()
deberia arrojar los datos que hay guardados en la DB

registro1 =  Clase(campo1 = valor1, campo2 = valor2 ...)
registro1.save()


**Formato de JSON para crear usuario**

{"username": "lbmonroyj",
"password":"123456789",
"apellido": "Monroy",
"nombre": "Luis",
"email": "lbmonroyj@gmail.com",
"telefono": "31031531925",
"direccion": "Calle 4 # 85 - 13"
}


{"username": "santiago.mlondono4",
"password":"123456789",
"apellido": "Martinez",
"nombre": "Santiago",
"email": "santiago.mlonodono4@gmail.com",
"telefono": "3127492680",
"direccion": "Calle 4 # 85 - 15"
}

**Formato de JSON para crear producto**

{"nombre_producto": "papitas_fritas",
"presentacion":"1kg en bolsa",
"precio": "5400.15"
}

{"nombre_producto": "papitas_francesa",
"presentacion":"1kg en caja",
"precio": "4200.4"
}

{"nombre_producto": "Yucas_fritas",
"presentacion":"1kg en bolsa",
"precio": "4500.83"
}

{"nombre_producto": "papitas_criollas",
"presentacion":"1kg al vacio",
"precio": "6300.28"
}

**Formato de JSON para crear los estados**
{"descripcion": "pagado"
}

{"descripcion": "preparado"
}

{"descripcion": "congelado"
}

{"descripcion": "empacado"
}

{"descripcion": "enviado"
}

{"descripcion": "recibido"
}

**Formato de JSON para agregar al carrito**

{
    "id_usuario": 2,
    "productos_usuario": [
                        {"1" : 4}, 
                        {"2": 8}
]
}

** Para agregar el pedido manualmente para crear una prueba **

import django
from pf_app.models.pedido import Pedido
from pf_app.models.user import User
u = User.objects.all()
usuario = u.get(pk=1)
q = Pedido(id_usuario = usuario, total = 8)
q.save()

para hacer un push a heroku desde una rama se escribe:
    git push heroku <rama>:main
