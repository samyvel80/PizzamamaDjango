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

from api.mixin import StaffEditorPermissionsMixin
from .mix import UserQuerrySetMixin


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

class ListCreatePizzaView(
    generics.ListCreateAPIView,
    StaffEditorPermissionsMixin,
    UserQuerrySetMixin,
    ):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    #authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]# permet l'authentification par session
    #permission_classes = [permissions.IsAdminUser, IsStaffPermission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def perform_create(self, serializer):
        email = serializer.validated_data.pop('email')
        print(serializer.validated_data)
        #name = serializer.validated_data.get('nom')
        serializer.save(user=self.request.user) #on ajoute le user dans la sauvegarde

    #def get_queryset(self):
    #    qs = super().get_queryset()
    #    user = self.request.user
    #    return qs.filter(user=user)




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
