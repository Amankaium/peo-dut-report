from django.db import models


class Report(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
