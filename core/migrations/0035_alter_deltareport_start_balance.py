# Generated by Django 4.2.4 on 2023-10-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_alter_deltareport_actual_fuel_consumption_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deltareport',
            name='start_balance',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Остаток на начало'),
        ),
    ]
