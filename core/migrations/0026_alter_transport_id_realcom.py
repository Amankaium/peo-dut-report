# Generated by Django 4.2.4 on 2023-10-13 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_rename_name_realcom_transport_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='id_realcom',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
