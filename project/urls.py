"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('transports/', TransportListAPIView.as_view(), name='transports'),
    path('transports/<int:pk>/', TransportDetailAPIView.as_view(), name='transport'),

    path('reports/', ReportListAPIVew.as_view(), name='reports'),
    path('reports/<int:pk>/', ReportDetailAPIView.as_view(), name='report'),

    path('drivers/', DriverListAPIView.as_view(),name='drivers'),
    path('drivers/<int:pk>/', DriverDetailAPIView.as_view(),name='driver'),

    path('fuel_stations/', FuelStationsListAPIView.as_view(), name='fuel_stations'),
    path('fuel_stations/<int:pk>/', FuelStationsDetailAPIView.as_view(), name='fuel_station'),


    path('cards/', CardListAPIView.as_view(),name='cards'), 

    path('operation-types/', OperationTypeListAPIView.as_view(), name='operation-types'),
    path('operation-types/<int:pk>/', OperationTypeDetailAPIView.as_view(), name='operation-type'),

    path('fuel-types/', FuelTypeListAPIView.as_view(), name='fuel-types'),

 
]
