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
"precio": "8200.40"
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
"id_usuario": 1,
"productos": 3,
"cantidad": 6
}


para hacer un push a heroku desde una rama se escribe:
    git push heroku <rama>:main

    
**Edit a file, create a new file, and clone from Bitbucket in under 2 minutes**

When you're done, you can delete the content in this README and update the file with details for others getting started with your repository.

*We recommend that you open this README in another tab as you perform the tasks below. You can [watch our video](https://youtu.be/0ocf7u76WSo) for a full demo of all the steps in this tutorial. Open the video in a new tab to avoid leaving Bitbucket.*

---

## Edit a file

You’ll start by editing this README file to learn how to edit a file in Bitbucket.

1. Click **Source** on the left side.
2. Click the README.md link from the list of files.
3. Click the **Edit** button.
4. Delete the following text: *Delete this line to make a change to the README from Bitbucket.*
5. After making your change, click **Commit** and then **Commit** again in the dialog. The commit page will open and you’ll see the change you just made.
6. Go back to the **Source** page.

---

## Create a file

Next, you’ll add a new file to this repository.

1. Click the **New file** button at the top of the **Source** page.
2. Give the file a filename of **contributors.txt**.
3. Enter your name in the empty file space.
4. Click **Commit** and then **Commit** again in the dialog.
5. Go back to the **Source** page.

Before you move on, go ahead and explore the repository. You've already seen the **Source** page, but check out the **Commits**, **Branches**, and **Settings** pages.

---

## Clone a repository

Use these steps to clone from SourceTree, our client for using the repository command-line free. Cloning allows you to work on your files locally. If you don't yet have SourceTree, [download and install first](https://www.sourcetreeapp.com/). If you prefer to clone from the command line, see [Clone a repository](https://confluence.atlassian.com/x/4whODQ).

1. You’ll see the clone button under the **Source** heading. Click that button.
2. Now click **Check out in SourceTree**. You may need to create a SourceTree account or log in.
3. When you see the **Clone New** dialog in SourceTree, update the destination path and name if you’d like to and then click **Clone**.
4. Open the directory you just created to see your repository’s files.

Now that you're more familiar with your Bitbucket repository, go ahead and add a new file locally. You can [push your change back to Bitbucket with SourceTree](https://confluence.atlassian.com/x/iqyBMg), or you can [add, commit,](https://confluence.atlassian.com/x/8QhODQ) and [push from the command line](https://confluence.atlassian.com/x/NQ0zDQ).
