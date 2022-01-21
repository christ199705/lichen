from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('data/cuisine/all',views.cuisine_all),
    path('data/cuisine/<int:sid>',views.cuisine),
    path('data/cuisine/increment',views.put_increment),
]