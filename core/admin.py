from django.contrib import admin
from core.models import *

admin.site.register(Report)
admin.site.register(Station)
admin.site.register(Transport)
admin.site.register(DriversName)
admin.site.register(Card)
admin.site.register(OperationType)
admin.site.register(FuelType)
admin.site.register(DeltaReport)
@admin.register(CardOperation)
class CardOperationAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'station',
        'card',
        'fuel_type',
        'operation_type',
        'balance_before',
        'balance_after',
        'dose',
        'price_som',
        'sum_som',
    ]    

admin.site.register(ExcelSource)
