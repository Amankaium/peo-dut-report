from django.db import models
from .station import Station
from .card import Card
from .fuel import FuelType
from .operation import OperationType


class CardOperation(models.Model):
    date = models.DateTimeField('Дата')
    station = models.ForeignKey(to=Station, on_delete=models.CASCADE)
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(to=FuelType, on_delete=models.CASCADE)
    operation_type = models.ForeignKey(to=OperationType, on_delete=models.CASCADE)
    balance_before = models.DecimalField('Баланс до', max_digits=10, decimal_places=2)
    balance_after = models.DecimalField('Баланс после', max_digits=10, decimal_places=2)
    dose = models.DecimalField('Доза', max_digits=10, decimal_places=2)
    price_som = models.DecimalField('Цена, сом', max_digits=10, decimal_places=2)
    sum_som = models.DecimalField('Сумма, сом', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Операция по карте'
        verbose_name_plural = 'Операции по карте'
    
# Поля на момент 06.09.2023
    # Дата
    # АЗС
    # Карта
    # Вид топлива
    # Вид операции
    # Баланс до
    # Баланс после
    # Доза
    # Цена, Сом
    # Сумма Сом
