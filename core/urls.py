from django.urls import path
from .views import *


urlpatterns = [
    path('', GetDataView.as_view(), name='home'),
    path('get-drivers', GetDriversListView.as_view(), name='drivers'),
    path('transport/<int:pk>/', TransportInfoView.as_view(), name='transports-info'),
    path('get-drivers/', GetDriversListView.as_view(), name='drivers-list'),
    path('get-transports/', GetTransportView.as_view(), name='transports-list'),
    path('get_fuel_type/', GetFuelTypeView.as_view(), name='get_fuel_type'),
    path('cards-list/', CardListView.as_view(), name='cards-list'),
    path('stations-list/', StationListView.as_view(), name='stations-list'),
    path('drivers-add/', DriversAddView.as_view(), name='drivers-add'),
]
