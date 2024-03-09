from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    
]