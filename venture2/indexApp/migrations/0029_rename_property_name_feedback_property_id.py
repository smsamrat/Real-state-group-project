# Generated by Django 4.1.2 on 2022-10-29 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0028_rename_post_property_post_feedback_property_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='property_name',
            new_name='property_id',
        ),
    ]