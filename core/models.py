from django.db import models


class Transport(models.Model):
    mark = models.CharField(max_length=20)
    number = models.CharField(unique=True, max_length=20)
    trailer = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Транспортное средство"
        verbose_name_plural = "Транспортные средства"


class Station(models.Model):
    name = models.CharField('Наименование', max_length=80, null=True, blank=False)
    id_realcom = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'АЗС'
        verbose_name_plural = 'АЗС'


class Report(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'


class DriversName(models.Model):
    full_name = models.CharField(blank=False, max_length=55)

    class Meta:
        verbose_name = 'Ф.И.О'


class Card(models.Model):
    id_realcom = models.PositiveIntegerField()
    number = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'


class FuelType(models.Model):
    fuel = models.CharField(blank=False, max_length=20)
    id_realcom = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Вид топлива'
        verbose_name_plural = 'Виды топлива'


class OperationType(models.Model):
    id_realcom = models.PositiveIntegerField(null=False, blank=False)
    name = models.CharField("Вид операции",max_length=20)

    class Meta:
        verbose_name = 'Вид операции'
        verbose_name_plural = 'Виды операции'


class CardOperation(models.Model):
    date = models.DateTimeField('Дата', auto_now_add=True)
    station = models.ForeignKey(to=Station, on_delete=models.CASCADE)
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(to=FuelType, on_delete=models.CASCADE)
    operation_type = models.ForeignKey(to=OperationType, on_delete=models.CASCADE)
    balance_before = models.DecimalField('Баланс до', max_digits=19, decimal_places=10)
    balance_after = models.DecimalField('Баланс после', max_digits=19, decimal_places=10)
    dose = models.DecimalField('Доза', max_digits=19, decimal_places=10)
    price_som = models.DecimalField('Цена, сом', max_digits=19, decimal_places=10)
    sum_som = models.DecimalField('Сумма, сом', max_digits=19, decimal_places=10)

    class Meta:
        verbose_name = 'Операция по карте'
        verbose_name_plural = 'Операции по карте'





