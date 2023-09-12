from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class ExcelSource(models.Model):
    excel_file = models.FileField(upload_to=f'excel/{datetime.now().year}/{datetime.now().month}/')
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by.username

