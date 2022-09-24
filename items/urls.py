from django.contrib import admin
from django.urls import path, include

import items
from items import views

urlpatterns = [
    path('', views.index, name='index')
]
