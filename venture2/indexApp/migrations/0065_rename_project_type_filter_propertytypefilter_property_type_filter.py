# Generated by Django 4.1.2 on 2022-11-07 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0064_remove_propertytypefilter_project_type_filter_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertytypefilter',
            old_name='project_type_filter',
            new_name='property_type_filter',
        ),
    ]
