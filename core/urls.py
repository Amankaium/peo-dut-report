from django.urls import path
from .views import *



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('drivers', GetDriversListView.as_view(), name='get-drivers'),
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
    path('transport-id-realcom-add/', TransportIdRealcomView.as_view(), name='transport-id-realcom-add'),
    path('transport-id-realcom-get/', TransportIdRealcomGetView.as_view(), name='transport-id-realcom-get'),
    path('id-realcom-add-drivers/', DriversIdRealcomView.as_view(), name='id-realcom-add-drivers'),
    path('id-realcom-get-list-drivers/', DriversRealcomView.as_view(), name='id-realcom-get-list-drivers'),
    path('delta-reports-add/', DeltaReportAddView.as_view(), name='delta-reports-add'),
    path('update-delta-report/<int:id>/', DeltaReportUpdateView.as_view(), name='delta-reports-update'),
    path('ktg-parser/', KTGParserView.as_view(), name='ktg-parser'),
]
