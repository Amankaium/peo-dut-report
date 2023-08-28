from django.db import models

class Name(models.Model):
    name = models.CharField('Наименование', max_length=80, null=True, blank=False)
    id = models.PositiveIntegerField('id', primary_key=True)
    class Meta:
        verbose_name = 'Наименование:'
        verbose_name_plural = 'Наименования:'
# Create your models here.

class ReportDate(models.Model):
    start_date = models.DateTimeField(auto_now_add=True, blank=False)
    end_date = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        verbose_name = 'date_report'
        verbose_name_plural = 'date_reports'


class DriversName(models.Model):
    full_name = models.CharField(blank=False, max_length=55)

    class Meta:
        verbose_name = 'Ф.И.О'
