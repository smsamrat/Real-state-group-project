# Generated by Django 4.1.2 on 2022-10-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0012_rename_city_district_rename_country_division'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_img', models.ImageField(upload_to='blog_images')),
                ('title', models.CharField(max_length=250)),
                ('details', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]