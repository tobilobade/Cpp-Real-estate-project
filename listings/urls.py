from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('sell/', views.sell_house, name='sell_house'),
    path('delete/<int:house_id>/', views.delete_house, name='delete_house'),
    path('property/<int:house_id>/', views.property_detail, name='property_detail'),
    path('buy-houses/', views.render_buy_houses, name='render_buy_houses'),
    path('rent-houses/', views.render_rent_houses, name='render_rent_houses'),
    path('view-more-properties/', views.view_more_properties, name='view_more_properties'),
    # Add more URL patterns as needed
]

urlpatterns += staticfiles_urlpatterns()
