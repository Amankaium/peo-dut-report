from django.db import models


class Transport(models.Model):
    mark = models.CharField(max_length=20, null=True, blank=True)
    number = models.CharField(null=True, blank=True, max_length=20)
    trailer = models.CharField(max_length=20, blank=True, null=True)
    id_realcom = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Транспортное средство"
        verbose_name_plural = "Транспортные средства"
    
    def __str__(self):
        return self.name

