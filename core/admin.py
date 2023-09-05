from django.contrib import admin
from .models import *

admin.site.register(Report)
admin.site.register(Station)
admin.site.register(Transport)
admin.site.register(DriversName)
admin.site.register(Card)
admin.site.register(OperationType)
admin.site.register(FuelType)
admin.site.register(CardOperation)

