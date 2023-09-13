from django.db import models


class Delta_report(models.Model):
    delta = models.IntegerField()

    class Meta:
        verbose_name = 'Отклонение'
        verbose_name_plural = 'Отклонения'

    def __str__(self):
        return str(self.delta)