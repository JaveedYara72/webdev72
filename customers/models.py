from django.db import models

class pizza(models.Model):
    pizzaName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class pizzaType(models.Model):
    pizzaTypeName = models.CharField(max_length=255)
class cheese(models.Model):
    cheeseName = models.CharField(max_length=255)

class toppings(models.Model):
    toppingName = models.CharField(max_length=255)

