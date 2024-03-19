from django.http import HttpResponse
from django.template import loader

from rest_framework import viewsets
from .models import pizza,pizzaType, cheese, toppings
from .serializers import PizzaSerializer,PizzaTypeSerializer, CheeseSerializer, ToppingsSerializer
from django.views.decorators.csrf import csrf_exempt
import json


class PizzaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pizza.objects.all()
    serializer_class = PizzaSerializer

class PizzaTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pizzaType.objects.all()
    serializer_class = PizzaTypeSerializer

class CheeseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = cheese.objects.all()
    serializer_class = CheeseSerializer

class ToppingsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = toppings.objects.all()
    serializer_class = ToppingsSerializer


def customers(request):
  # Define context data to pass to the template
  context = {
      'pizzas': PizzaViewSet.queryset,
      'pizza_types': PizzaTypeViewSet.queryset,
      'cheeses': CheeseViewSet.queryset,
      'toppings': ToppingsViewSet.queryset,
  }
  # Variables in Django, youll pass it like this and parse it as pizzaname in
  template = loader.get_template('index.html')
  return HttpResponse(template.render(context,request))

