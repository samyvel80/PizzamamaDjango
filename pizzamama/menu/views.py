from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# IMPORT POUR faire une API REST
from .serializers import PizzaSerializerApiView, PizzaSerializer
from django.forms.models import model_to_dict
from rest_framework import generics, permissions, authentication
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .authentication import TokenAuthentication

import json

from api.permissions import IsStaffPermission


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

class PizzaViewset(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class ListCreatePizzaView(generics.ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]# permet l'authentification par session
    permission_classes = [permissions.IsAdminUser, IsStaffPermission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def perform_create(self, serializer):
        name = serializer.validated_data.get('nom')
        serializer.save()

    def get_queryset(self):
        #queryset = Pizza.objects.all()
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        nom = self.request.query_params.get('nom')
        if nom is not None:
            return super().get_queryset().filter(nom__icontains=nom)
        return super().get_queryset()
        #return queryset




class RetrievePizzaView(generics.RetrieveAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
class UpdatePizzaView(generics.UpdateAPIView):

    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        nom = serializer.validated_data.get('nom')
        ingredients = serializer.validated_data.get('ingredients') or None
        if ingredients is None:
            ingredients = nom
        serializer.save(ingredients=ingredients)



class DeletePizzaView(generics.DestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    lookup_field = 'pk'

@api_view(['GET','POST'])
def api_view(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = PizzaSerializerApiView(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return ({"details": "invalid data"})
    query = Pizza.objects.all()
    #query = Pizza.objects.all().order_by('?').first()
    data ={}
    if query:
      #  data = model_to_dict(query, fields={'nom'})
        serializer = PizzaSerializerApiView(query,many=True)
    #print(request.headers)

    return Response(serializer.data)
'''
@api_view(['POST'])
def api_view(request, *args, **kwargs):
    data = request.data
    return Response(data)

@api_view(['POST'])
def api_view(request, *args, **kwargs):

    serializer = PizzaSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    else:
        return({"details":"invalid data"})
'''
