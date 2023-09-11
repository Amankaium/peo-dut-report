from django.urls import path
from .views import *


urlpatterns = [
    path('', GetDataView.as_view(), name='home'),
    path('get-drivers', GetDriversListView.as_view(), name='drivers'),
    path('get-transports/', GetTransportView.as_view(), name='get-transports'),
    path('cards-list/', CardListView.as_view(), name='cards'),
]