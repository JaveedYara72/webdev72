from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PizzaViewSet,PizzaTypeViewSet, CheeseViewSet, ToppingsViewSet

router = DefaultRouter()
router.register(r'getpizzas', PizzaViewSet)
router.register(r'getpizzatypes', PizzaTypeViewSet)
router.register(r'getcheeses', CheeseViewSet)
router.register(r'gettoppings', ToppingsViewSet)


urlpatterns = [
    path('', views.customers, name='customers'),
    path('', include(router.urls)),
]