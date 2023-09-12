from django.db import models


class DriversName(models.Model):
    full_name = models.CharField(blank=False, max_length=55)

    class Meta:
        verbose_name = 'Ф.И.О'
    
    def __str__(self):
        return self.full_name