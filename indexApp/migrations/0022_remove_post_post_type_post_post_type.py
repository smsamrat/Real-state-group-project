# Generated by Django 4.1.2 on 2022-10-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0021_property_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.ManyToManyField(related_name='pro_type', to='indexApp.property_type'),
        ),
    ]
