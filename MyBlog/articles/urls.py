from django.contrib import admin
from django.urls import path, include
from .views import articles_view

urlpatterns = [
    path('', articles_view),
]
