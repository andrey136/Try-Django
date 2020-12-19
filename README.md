## Virtual Environment

### Creating virtual environment

* virtualenv -p python3 .
* source bin/activate (or .\Scripts\activate)
* pip3 install django==2.0.7

### Activating virtual environment

* cd django-project-folder
* source bin/activate  (or .\Scripts\activate)
* deactivate

### Looking at the requirements

* pip3 freeze

It's important to use virtual environment for your projects for several reasons.
I. it keeps all the requirements seperate.

### 3 ways to create a virtual environment

* virtualenv venv
* virtualenv venv2 -p python3
(To find the location where python3 is intalled: which python3)
(Add the path to the command)
* virtualenv venv3 -p python3_path
### The 4th method to create virtual environment

* mkdir venv4
* cd venv4
* virtualenv . -p python3


## Django Project

### First Steps 

* mkdir src
* cd src
* django-admin startproject trydjango . 
* (__name of the project__: trydjango, __current folder__: .)
* python manage.py runserver

### Running our database

* python manage.py migrate

## Creating an app

### Built-in components

* Apps are pieces or components of a bigger django project

* In setting.py file in INSTALLED_APPS you put third party apps or your own

### Further commands

* python manage.py migrate
* python manage.py createsuperuser
* Then authorize in /admin

### Adding apps

* python manage.py startapp products
* python manage.py startapp cart
* python manage.py startapp blog
* python manage.py startapp profiles

### Creating Models

* Put this code in products/models.py

class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()

* Add products to the ISTALLED_APPS list in settings.py

