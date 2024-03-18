from django.db import models

class Customer(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=12)
  address = models.CharField(max_length=255)

class PizzaBase(models.Model):
    name = models.CharField(max_length=100)

class Cheese(models.Model):
    name = models.CharField(max_length=100)

class Topping(models.Model):
    name = models.CharField(max_length=100)