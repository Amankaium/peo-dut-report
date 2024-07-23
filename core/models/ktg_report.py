from .transport import Transport
from django.db import models


class KTGReport(models.Model):
    transport = models.ForeignKey(
        to=Transport,
        on_delete=models.CASCADE,
    )
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    day = models.DateField()
    trip_mileage = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Пробег в поездках", null=True, blank=True)
    dart_spending = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Потрачено по ДАРТ", null=True, blank=True)
    dut_spending = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Потрачено по ДУТ", null=True, blank=True)
    avg_dart_spending = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ср. расход по ДАРТ", null=True, blank=True)
    avg_dut_spending = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ср. расход по ДУТ", null=True, blank=True)
    refilled = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Заправлено", null=True, blank=True)
    leaked = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Слито", null=True, blank=True)
    is_working = models.BooleanField(default=True)

    def __str__(self):
        return self.transport
