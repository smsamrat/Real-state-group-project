# Generated by Django 4.1.2 on 2022-11-26 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0076_alter_area_options_alter_district_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertypost',
            name='post_type',
            field=models.ManyToManyField(blank=True, related_name='pro_type', to='indexApp.property_type'),
        ),
    ]