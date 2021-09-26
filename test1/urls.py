from django.urls import path, include
from .views import helloAPI, WriteTextList

urlpatterns = [
    path("hello/", helloAPI),
    path("writetext", WriteTextList)
]