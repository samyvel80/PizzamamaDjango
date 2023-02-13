from django.urls import path
#from . import views
from .views import ListCreatePizzaView, UpdatePizzaView, RetrievePizzaView, DeletePizzaView
from .views import api_view,index


app_name = 'menu'

urlpatterns = [
    path('', index, name="index"),
    path('api_view/', api_view, name='api_view'),
    path('create-list/', ListCreatePizzaView.as_view()),
    path('<int:pk>/update/', UpdatePizzaView.as_view(), name="update"),
    path('<int:pk>/retrieve/', RetrievePizzaView.as_view(), name="retrieve"),
    path('<int:pk>/delete/', DeletePizzaView.as_view(), name="delete"),


]