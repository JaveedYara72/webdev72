from django.contrib import admin
# import the models and register them here
from .models import pizza,pizzaType,cheese,toppings

# Register your models here.
admin.site.register(pizza)
admin.site.register(pizzaType)
admin.site.register(cheese)
admin.site.register(toppings)