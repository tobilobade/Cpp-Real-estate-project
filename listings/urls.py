from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # Add more URL patterns as needed
]
