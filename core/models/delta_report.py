from django.db import models
from core.models import Transport
from .excel_source import ExcelSource
from datetime import datetime

months = (
            (1, "Январь"),
            (2, "Февраль"),
            (3, "Март"),
            (4, "Апрель"),
            (5, "Май"),
            (6, "Июнь"),
            (7, "Июль"),
            (8, "Август"),
            (9, "Сентябрь"),
            (10, "Октябрь"),
            (11, "Ноябрь"),
            (12, "Декабрь"),
        )

class MonthReport(models.Model):
    source = models.OneToOneField(ExcelSource, models.PROTECT)
    month = models.IntegerField(
        verbose_name='Месяц',
        default=datetime.now().month,
        choices=months
    )
    year = models.IntegerField(default=datetime.now().year, verbose_name='Год')

    class Meta:
        unique_together = [['month', 'year']]
        ordering = ['year', 'month']

    def __str__(self):
        return f"Отчёт {months[int(self.month)-1][1]} {self.year}"


class DeltaReport(models.Model):
    month_report = models.ForeignKey(MonthReport, models.PROTECT, null=True)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, verbose_name="Объект транспорт")
    vehicle_name = models.CharField(max_length=20, verbose_name="Наименование ТС (название с файла)")
    period_start = models.DateTimeField(verbose_name="Начало периода")
    period_end = models.DateTimeField(verbose_name="Конец периода")
    fact_km = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Факт КМ")
    odometer_mileage = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Пробег по одометру", null=True, blank=True)
    trip_mileage = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Пробег в поездках", null=True, blank=True)
    start_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток на начало")
    start_level = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Нач. уровень", null=True, blank=True)
    fueling_gsm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Заправка ГСМ")
    total_refueled = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Всего заправлено", null=True, blank=True)
    actual_fuel_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Факт Расход топлива (литр)")
    norm_fuel_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Норма Расход топлива (литр)")
    departure = models.CharField(verbose_name="Напр.", max_length=55, null=True, blank=True)
    avg_trip_dut_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ср. расход по ДУТ в поездках", null=True, blank=True)
    avg_dut_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ср. расход по ДУТ (весь пробег)", null=True, blank=True)
    actual = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="По факту", null=True, blank=True)
    fuel_calculation_norm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Калькуляция нормы расхода")
    departure_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток по пут.листу")
    end_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток на конец", null=True, blank=True)
    end_level = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Кон. уровень", null=True, blank=True)
    end_mech_balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток кон.мех.")
    difference = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Разница", null=True, blank=True)
    deficiency = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Недостача/Излишек")
    total_fuel_drained = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Всего топлива слито", null=True, blank=True)
    note = models.TextField(blank=True, null=True, verbose_name="Примечание")

    class Meta:
        unique_together = [['month_report', 'transport']]

