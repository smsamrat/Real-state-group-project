# Generated by Django 4.1.2 on 2022-11-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0062_alter_feedback_is_feedback_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='is_feedback_show',
            field=models.BooleanField(default=False),
        ),
    ]
