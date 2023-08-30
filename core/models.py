from django.db import models


class Transport(models.Model):
    mark = models.CharField(max_length=20)
    number = models.CharField(unique=True, max_length=20)
    trailer = models.CharField(max_length=20, blank=True)
    class Meta:
        verbose_name = "Транспортное средство"
        verbose_name_plural = "Транспортные средства"


class GSM(models.Model):
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
    id_realcom = models.PositiveIntegerField(null=False, blank=False)
    number = models.PositiveIntegerField(default=0)

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

