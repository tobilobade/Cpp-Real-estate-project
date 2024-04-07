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
    path('subscribe-to-newsletter/', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    path('update/<int:house_id>/', views.update_house, name='update_house'),
    path('search/', views.search_view, name='search_view'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('get-ip-location/', views.get_ip_location_view, name='get_ip_location'),
]

urlpatterns += staticfiles_urlpatterns()
