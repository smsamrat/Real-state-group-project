# Generated by Django 4.1.2 on 2022-10-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0002_location_location_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='Agent_img/')),
                ('name', models.CharField(max_length=250)),
                ('disignation', models.CharField(max_length=250)),
                ('address', models.EmailField(max_length=250)),
                ('mobile', models.IntegerField()),
                ('fax', models.IntegerField()),
            ],
        ),
    ]
