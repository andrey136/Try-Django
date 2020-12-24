from django.contrib import admin

# Register your models here.
from .models import Fruit
from .models import Berry

admin.site.register(Fruit)
admin.site.register(Berry)