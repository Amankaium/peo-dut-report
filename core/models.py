from django.db import models

# Create your models here.

class ReportDate(models.Model):
    start_date = models.DateTimeField(auto_now_add=True, blank=False)
    end_date = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        verbose_name = 'star_date'
        verbose_name_plural = 'end_date'
