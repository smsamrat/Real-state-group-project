# Generated by Django 4.1.2 on 2022-10-22 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0011_country_city_area'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='City',
            new_name='District',
        ),
        migrations.RenameModel(
            old_name='Country',
            new_name='Division',
        ),
    ]
