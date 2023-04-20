from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('colors', views.colors, name='colors'),
    path('change_dashboard_screen', views.change_dashboard_screen, name='change_dashboard_screen'),
]