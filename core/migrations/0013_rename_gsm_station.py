# Generated by Django 4.2.4 on 2023-09-04 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_card_number_alter_transport_trailer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GSM',
            new_name='Station',
        ),
    ]
