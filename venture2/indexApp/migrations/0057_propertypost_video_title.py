# Generated by Django 4.1.2 on 2022-11-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0056_alter_propertypost_broucher'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertypost',
            name='video_title',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
