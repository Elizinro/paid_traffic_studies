from django.urls import path
from . import views

urlpatterns = [
    path('change_me', views.change_me, name='change_me'),
]