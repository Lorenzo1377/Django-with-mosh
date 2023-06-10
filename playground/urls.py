from django.urls import path
from .views import hello
from .views import my_name

urlpatterns = [
    path("hello", hello) ,
]