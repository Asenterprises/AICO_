from django.urls import path
from . import views

app_name = 'quality'

urlpatterns = [
    path('', views.index, name='index'),
    path('quality_check/', views.quality_check, name='quality_check'),
    path('quality_report/', views.quality_report, name='quality_report'),
]