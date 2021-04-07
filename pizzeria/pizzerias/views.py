from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    """Home page for pizzeria"""
    return render(request, 'pizzerias/index.html')

def pizzas(request):
    """Show all pizzas"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzerias/pizzas.html', context)

def pizza(request, pizza_id):
    """Show a single pizza and its toppings"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzerias/pizza.html', context)
