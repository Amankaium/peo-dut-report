from django.db import models
from core.models import Transport

class DeltaReport(models.Model):
    date = models.DateField()
    description = models.TextField()
    transport = models.ForeignKey(Transport,on_delete=models.CASCADE)

    def __str__(self):
        return self.description