# Generated by Django 4.2.4 on 2023-08-30 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_driversname'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel', models.CharField(max_length=20)),
                ('id_realcom', models.PositiveIntegerField()),
            ],
        ),
    ]
