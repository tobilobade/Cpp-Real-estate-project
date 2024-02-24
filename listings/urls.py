from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # Add more URL patterns as needed
]

urlpatterns += staticfiles_urlpatterns()
