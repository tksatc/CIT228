"""Defines URL patterns for pizzerias"""

from django.urls import path

from . import views

app_name = 'pizzerias'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # A page that shows all pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # Detail page for a single pizza
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]