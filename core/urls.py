from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', GetDataView.as_view(), name='home'),
    path('get-drivers', GetDriversListView.as_view(), name='drivers'),
    path('driver/<int:pk>/', DriverDetailView.as_view(), name='driver-detail'),
    path('transport/<int:pk>/', TransportInfoView.as_view(), name='transports-info'),
    path('get-drivers/', GetDriversListView.as_view(), name='drivers-list'),
    path('get-transports/', GetTransportView.as_view(), name='transports-list'),
    path('get_fuel_type/', GetFuelTypeView.as_view(), name='get_fuel_type'),
    path('cards-list/', CardListView.as_view(), name='cards-list'),
    path('stations-list/', StationListView.as_view(), name='stations-list'),
    path('drivers-add/', DriversAddView.as_view(), name='drivers-add'),
    path('stations-add/', StationAddView.as_view(), name='stations-add'),
    path('transport-add/', TransportAddView.as_view(), name='transport-add'),
    path('cards-add/', CardAddView.as_view(), name='cards-add'),
    path('card-operations/', views.CardOperationAddView.as_view(), name='card-operation-list'),
    path('transports/', views.TransportAddView.as_view(), name='transport-list'),
]




