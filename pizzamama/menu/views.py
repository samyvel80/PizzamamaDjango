from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

# EXERCICE
# Les pizzas : Végétarienne : 8.5€, Poulet champignons : xxx, 4 fromages, Carnivore


def index(request):
    '''pizzas = Pizza.objects.all()
    pizzas_names_and_prices = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizzas_names_and_prices_str = ", ".join(pizzas_names_and_prices)
    return HttpResponse("Les pizzas : " + pizzas_names_and_prices_str)'''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas': pizzas})