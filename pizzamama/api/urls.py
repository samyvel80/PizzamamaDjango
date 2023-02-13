
from django.urls import path
from .views import api_pizza

urlpatterns = [
    path('api_view/', api_pizza),

]