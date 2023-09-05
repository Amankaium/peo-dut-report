from django.db import models


class Station(models.Model):
    name = models.CharField('Наименование', max_length=80, null=True, blank=False)
    id_realcom = models.PositiveIntegerField(null=False, blank=False)
    class Meta:
        verbose_name = 'АЗС'
        verbose_name_plural = 'АЗС'
