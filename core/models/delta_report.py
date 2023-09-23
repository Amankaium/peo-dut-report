from django.db import models
from core.models import Transport

class DeltaReport(models.Model):
    date = models.DateField()
    description = models.TextField()
    transport = models.ForeignKey(Transport,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class DeltaReport(models.Model):
    vehicle_name = models.CharField(max_length=20, verbose_name="Наименование ТС")
    period_start = models.DateTimeField(verbose_name="Начало периода")
    period_end = models.DateTimeField(verbose_name="Конец периода")
    fact_km = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Факт КМ")
    odometer_mileage = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Пробег по одометру")
    trip_mileage = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Пробег в поездках")
    start_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток на начало")
    start_level = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Нач. уровень")
    fueling_gsm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Заправка ГСМ")
    total_refueled = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Всего заправлено")
    actual_fuel_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Факт Расход топлива (литр)")
    norm_fuel_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Норма Расход топлива (литр)")
    departure = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Напр.")
    avg_trip_dut_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ср. расход по ДУТ в поездках")
    actual = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="По факту")
    fuel_calculation_norm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Калькуляция нормы расхода")
    departure_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток по пут.листу")
    end_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток на конец")
    end_level = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Кон. уровень")
    end_mech_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток кон.мех.")
    difference = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Разница")
    deficiency = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Недостача")
    surplus = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Излишек")
    total_fuel_drained = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Всего топлива слито")


