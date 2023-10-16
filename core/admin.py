from django.contrib import admin
from core.models import *

admin.site.register(Report)
admin.site.register(Station)
admin.site.register(DriversName)
admin.site.register(Card)
admin.site.register(OperationType)
admin.site.register(FuelType)
admin.site.register(MonthReport)


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_realcom', 'name']
    search_fields = ['name']
    list_per_page = 300


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

@admin.register(DeltaReport)
class DeltaReportAdmin(admin.ModelAdmin):
    list_filter = ["month_report", "transport"]

    list_display = [
        'month_report',
        'transport',
        'vehicle_name',
        'period_start',
        'period_end',
        'fact_km',
        'odometer_mileage',
        'trip_mileage',
        'start_balance',
        'start_level',
        'fueling_gsm',
        'total_refueled',
        'actual_fuel_consumption',
        'norm_fuel_consumption',
        'departure',
        'avg_trip_dut_consumption',
        'actual',
        'fuel_calculation_norm',
        'departure_balance',
        'end_balance',
        'end_level',
        'end_mech_balance',
        'difference',
        'deficiency',
        'total_fuel_drained',
        'note'
    ]

