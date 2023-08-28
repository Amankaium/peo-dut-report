from django.db import models

# Create your models here.
class transport(models.Model):
    mark = models.CharField(max_length=20)
    number = models.CharField(unique=True, max_length=20)
    trailer = models.CharField(max_length=20, blank=True)
    class Meta:
        verbose_name = "Транспортное средство"
        verbose_name_plural = "Транспортные средства"