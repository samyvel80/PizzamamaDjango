"""pizzamama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#for displaying static page import repath
from django.urls import path, include,re_path
from rest_framework.authtoken.views import obtain_auth_token
######for displaying static page collectstatic
from django.conf import settings
from django.views.static import serve
#############################################

#from rest_framework import routers
#from menu.views import PizzaViewset
#router = routers.SimpleRouter()
#router.register('PizzaViewset', PizzaViewset, basename='pizzaviewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu-pizza/', include('menu.urls')),
    path('', include('main.urls')),
    #path('pizza-api/', include('router.urls')),
    path('pizza/', include('pizzamama.routers')),
    path('auth', obtain_auth_token),
    #for displaying static page
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
