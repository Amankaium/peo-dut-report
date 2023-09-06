from django.db import models


class FuelType(models.Model):
    fuel = models.CharField(blank=False, max_length=20)
    id_realcom = models.PositiveIntegerField(null=False, blank=False)
    
    class Meta:
        verbose_name = 'Вид топлива'
        verbose_name_plural = 'Виды топлива'
    
    def __str__(self):
        return self.fuel