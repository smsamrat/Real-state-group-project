# Generated by Django 4.1.2 on 2022-10-30 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0043_aboutus_description_aboutus_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutLookingSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'AboutLookingSection',
                'verbose_name_plural': 'About looking section',
            },
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'AboutUs', 'verbose_name_plural': 'About Us'},
        ),
    ]
