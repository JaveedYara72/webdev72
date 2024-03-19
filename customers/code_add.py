# models.py
from django.db import models

class Pizza(models.Model):
    pizzaName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class PizzaBase(models.Model):
    pizzaTypeName = models.CharField(max_length=255)

class Cheese(models.Model):
    cheeseName = models.CharField(max_length=255)

class Topping(models.Model):
    toppingName = models.CharField(max_length=255)

class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza, through="OrderDetail")
    created_at = models.DateTimeField(auto_now_add=True)

class OrderDetail(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizzaBase = models.ForeignKey(PizzaBase, on_delete=models.SET_NULL, null=True)
    cheese = models.ForeignKey(Cheese, on_delete=models.SET_NULL, null=True)
    toppings = models.ManyToManyField(Topping)


# add serializers to the view.

# views.py
from django.http import JsonResponse
from .models import Order, Pizza, PizzaBase, Cheese, Topping, OrderDetail
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.create()
        for pizza_data in data.get('pizzas', []):
            pizza = Pizza.objects.get(id=pizza_data['pizza_id'])
            pizza_base = PizzaBase.objects.get(id=pizza_data['base_id'])
            cheese = Cheese.objects.get(id=pizza_data['cheese_id'])
            order_detail = OrderDetail.objects.create(pizza=pizza, order=order, pizzaBase=pizza_base, cheese=cheese)
            for topping_id in pizza_data['topping_ids']:
                topping = Topping.objects.get(id=topping_id)
                order_detail.toppings.add(topping)
        return JsonResponse({"success": True, "order_id": order.id}, status=201)
    return JsonResponse({"error": "Invalid request"}, status=400)


# Implementing Track order API
def track_order(request, order_id):
    try:
        order = Order.objects.prefetch_related('pizzas').get(id=order_id)
        order_details = []
        for detail in order.orderdetail_set.all():
            order_details.append({
                'pizza': detail.pizza.pizzaName,
                'base': detail.pizzaBase.pizzaTypeName,
                'cheese': detail.cheese.cheeseName,
                'toppings': list(detail.toppings.values_list('toppingName', flat=True))
            })
        return JsonResponse({"order_details": order_details}, status=200)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)

# Url configuration
# urls.py
from django.urls import path
from .views import add_order, track_order

urlpatterns = [
    path('api/add_order/', add_order, name='add_order'),
    path('api/track_order/<int:order_id>/', track_order, name='track_order')
]
