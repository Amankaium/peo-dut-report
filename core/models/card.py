from django.db import models


class Card(models.Model):
    id_realcom = models.PositiveIntegerField()
    number = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
    
    def __str__(self):
        return str(self.number)