# Generated by Django 4.2.4 on 2023-09-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_excelsource'),
    ]

    operations = [
        migrations.AddField(
            model_name='transport',
            name='id_realcom',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transport',
            name='name_realcom',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]