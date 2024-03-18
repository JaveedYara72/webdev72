from rest_framework import serializers
from .models import pizza,pizzaType, cheese, toppings

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = pizza
        fields = ['pizzaName']

class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = pizzaType
        fields = ['pizzaTypeName']

class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = cheese
        fields = ['cheeseName']

class ToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = toppings
        fields = ['toppingName']