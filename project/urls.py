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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import *

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet, basename='user')

station_router = DefaultRouter()
station_router.register(r'stations', StationViewSet, basename='station')

driversname_router = DefaultRouter()
driversname_router.register(r'driversname', DriverViewSet, basename='driversname')

transport_router = DefaultRouter()
transport_router.register('transports', TransportViewSet, basename='transport')

report_router = DefaultRouter()
report_router.register('reports', ReportViewSet, basename='report')

operation_router = DefaultRouter()
operation_router.register(r'operation-types', OperationTypeViewSet, basename='operation-type')

card_operation_router = DefaultRouter()
card_operation_router.register('card-operation', CardOperationViewSet, basename='card_operation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transports/', TransportListAPIView.as_view(), name='transports'),
    path('transports/<int:pk>/', TransportDetailAPIView.as_view(), name='transport'),
    path('transports-create/', TransportCreateAPIView.as_view(), name='transport-create'),
    path('reports/', ReportListAPIVew.as_view(), name='reports'),
    path('report-create/', ReportCreateAPIVew.as_view(), name='report-create'),
    path('report-update/<int:pk>/', ReportUpdateAPIVew.as_view(), name='report-update'),
    path('drivers/', DriverListCreateAPIView.as_view(), name='drivers'),
    path('reports/<int:pk>/', ReportDetailAPIView.as_view(), name='report'),
    path('report-update/<int:pk>/', ReportUpdateAPIVew.as_view(), name='report-update'),
    path('report-delete/<int:pk>/', ReportDeleteAPIVew.as_view(), name='report-delete'),
    path('report-generic/<int:pk>/', ReportAPIVew.as_view(), name='report-gen'),
    path('drivers/', DriverListCreateAPIView.as_view(),name='drivers'),
    path('drivers/<int:pk>/', DriverDetailAPIView.as_view(),name='driver'),
    path('fuel_stations/', FuelStationsListAPIView.as_view(), name='fuel_stations'),
    path('fuel_stations/<int:pk>/', FuelStationsDetailAPIView.as_view(), name='fuel_station'),
    path('cards/', CardListCreateAPIView.as_view(),name='cards'),
    path('operation-types/', OperationCreateTypeListAPIView.as_view(), name='operation-types'),
    path('operation-types/<int:pk>/', OperationTypeDetailAPIView.as_view(), name='operation-type'),
    path('fuel-types-detail/<int:pk>/', FuelTypeDetailAPIView.as_view(), name='fuel-types'),
    path('cards/<int:pk>/', CardDetailAPIView.as_view(), name='card'),
    path('fuel-types/', FuelTypeListAPIView.as_view(), name='fuel-types'),
    path('fuel-types-create/', FuelTypeCreateAPIView.as_view(), name='fuel-types-create/'),
    path('fuel-types-create/', FuelTypeCreateAPIView.as_view(), name='fuel-types-create/'),
    path('api/', include(user_router.urls)),
    path('api/', include(station_router.urls)),
    path('api/', include(driversname_router.urls)),
    path('api/', include(transport_router.urls)),
    path('api/', include(report_router.urls)),
    path('api/', include(operation_router.urls)),
    path('api/', include(card_operation_router.urls)),
]
