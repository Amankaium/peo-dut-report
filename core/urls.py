from django.urls import path
from .views import *


urlpatterns = [
    path('', GetDataView.as_view(), name='home'),
    path('get-transports/', GetTransportView.as_view(), name='get-transports'),
    path('get_fuel_type/', GetFuelTypeView.as_view(), name='get_fuel_type'),
    ]