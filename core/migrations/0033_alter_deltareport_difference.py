# Generated by Django 4.2.4 on 2023-10-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_monthreport_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deltareport',
            name='difference',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Разница'),
        ),
    ]
