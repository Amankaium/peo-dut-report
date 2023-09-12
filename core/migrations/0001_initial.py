# Generated by Django 4.2.4 on 2023-09-12 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_realcom', models.PositiveIntegerField()),
                ('number', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Карта',
                'verbose_name_plural': 'Карты',
            },
        ),
        migrations.CreateModel(
            name='DriversName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=55)),
            ],
            options={
                'verbose_name': 'Ф.И.О',
            },
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel', models.CharField(max_length=20)),
                ('id_realcom', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Вид топлива',
                'verbose_name_plural': 'Виды топлива',
            },
        ),
        migrations.CreateModel(
            name='OperationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_realcom', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=20, verbose_name='Вид операции')),
            ],
            options={
                'verbose_name': 'Вид операции',
                'verbose_name_plural': 'Виды операции',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True, verbose_name='Наименование')),
                ('id_realcom', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'АЗС',
                'verbose_name_plural': 'АЗС',
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=20, unique=True)),
                ('trailer', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Транспортное средство',
                'verbose_name_plural': 'Транспортные средства',
            },
        ),
        migrations.CreateModel(
            name='ExcelSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='excel/2023/9/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CardOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('balance_before', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Баланс до')),
                ('balance_after', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Баланс после')),
                ('dose', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Доза')),
                ('price_som', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена, сом')),
                ('sum_som', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма, сом')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.card')),
                ('fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.fueltype')),
                ('operation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.operationtype')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.station')),
            ],
            options={
                'verbose_name': 'Операция по карте',
                'verbose_name_plural': 'Операции по карте',
            },
        ),
    ]
