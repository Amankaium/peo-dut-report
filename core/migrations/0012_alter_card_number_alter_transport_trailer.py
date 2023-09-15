# Generated by Django 4.2.4 on 2023-09-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_merge_20230830_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='transport',
            name='trailer',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]