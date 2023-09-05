from django.db import models


class OperationType(models.Model):
    id_realcom = models.PositiveIntegerField(null=False, blank=False)
    name = models.CharField("Вид операции",max_length=20)
    class Meta:
        verbose_name = 'Вид операции'
        verbose_name_plural = 'Виды операции'
