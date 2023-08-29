from django.db import models

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

