from django.urls import path 
from .views import Register
from . import views

urlpatterns = [
   # path('',views.index, name= 'index'),
    path('register/',Register.as_view(),name = 'register'),
]