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

class Order(models.Model):
    pizzas = models.ManyToManyField(pizza, through="OrderDetail")
    created_at = models.DateTimeField(auto_now_add=True)

class OrderDetail(models.Model):
    pizza = models.ForeignKey(pizza, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizzaType = models.ForeignKey(pizzaType, on_delete=models.SET_NULL, null=True)
    cheese = models.ForeignKey(cheese, on_delete=models.SET_NULL, null=True)
    toppings = models.ManyToManyField(toppings)