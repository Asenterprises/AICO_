from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [
    path('', views.index, name='index'),
    path('inventory/', views.inventory, name='inventory'),
    path('shipment/', views.shipment, name='shipment'),
    path('receive/', views.receive, name='receive'),
]