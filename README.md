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

### Migrating dbs with projects and creating a super user(admin)

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
* Then save the settings.py file and models.py file

### Migrate commands

* As you change models.py save it!!!
* ALWAYS run these commands after making any changes to models.py

* python manage.py makemigrations
* python manage.py migrate

* Run in conjuction with each other every single time you make changes to models.py


from django.db import models
#Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    __summery     = models.TextField()__ --(new line in models.py)

## Create Product Objects in the Python shell

### Creating Object
 * python manage.py shell
 * from products.models import Product
 * Product.objects.all()
 * Product.objects.create()
 * Product.objects.create(title='New product 2', description='another one', price='19312', summary='sweet')

## New Model Fields



### Starting over

* To start over you need to delete all the files in migration folder except for the init.py in products app

* Delete sqlite db

* Check out https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.AutoField

### Changes in models.py

from django.db import models

#Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField()

### Further commands

* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser -- because we deleted our sqlite database

* python manage.py shell
* from products.models import Product
* Product.objects.create(title='Newer title', price=239.99, summary='Awesome sause')

## Change a model
* if blank attribute = False then the field is required to be filled



## ERRORS

### OperationalError at /admin/products/product/add/

Solution
* pip install django==2.1.5

### products.Product.title: (fields.E120) CharFields must define a 'max_length' attribute.

#Create your models here.
class Product(models.Model):
    title       = __models.CharField() # max_length = required__
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default='this is cool!')

* title = models.CharField(max_length=120) -- You must set max_width attribute with models.CharField() field type

### You are trying to add a non-nullable field 'featured' to product
This happens after changing the model of an APP without making any changes to the previous objects of this model in a database

Previous model:
#Create your models here.
class Product(models.Model):
    title       = __models.CharField() # max_length = required__
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default='this is cool!')

Current model:
#Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField()
    featured    = models.BooleanField()

>> There's at least two solutions
1. featured = models.BooleanField(null=True)
* Leaves this field empty in all the previous objects
1.  featured = models.BooleanField(default=True)
* Sets this field to true in all the previous objects
1. Choose one of the options provided in the shell
* 1
* True

### OperationalError at /admin/products/product/ no such column: products_product.featured

* python manage.py makemigrations
* python manage.py migrate