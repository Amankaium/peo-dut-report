# Generated by Django 4.2.4 on 2023-10-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_deltareport_departure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deltareport',
            name='actual',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='По факту'),
        ),
    ]
