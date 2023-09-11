from django.urls import path
from .views import *


urlpatterns = [
    path('', GetDataView.as_view(), name='home'),
    path('cards-list/', CardListView.as_view(), name='cards'),
    path('stations-list/', StationListView.as_view(), name='stations-list')
]