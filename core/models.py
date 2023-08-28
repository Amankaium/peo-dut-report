from django.db import models

class Name(models.Model):
    name = models.CharField('Наименование', max_length=80, null=True, blank=False)
    id = models.PositiveIntegerField('id', primary_key=True)
    class Meta:
        verbose_name = 'Наименование:'
        verbose_name_plural = 'Наименование:'