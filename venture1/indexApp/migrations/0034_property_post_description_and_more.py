# Generated by Django 4.1.2 on 2022-10-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0033_property_post_floor_plan_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_post',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='property_post',
            name='floor_plan_image',
            field=models.ImageField(blank=True, null=True, upload_to='floor_plan_image/'),
        ),
    ]