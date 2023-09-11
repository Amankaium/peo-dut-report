from django.urls import path
from .views import *


urlpatterns = [
    path('', GetDataView.as_view(), name='home'),
    path('get-drivers', GetDriversListView.as_view(), name='drivers'),
]