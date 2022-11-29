# Generated by Django 4.1.2 on 2022-10-25 08:54

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0013_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
                ('active_status', models.BooleanField(default=True)),
                ('job_description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('post_date', models.DateField()),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'ContactUs',
                'verbose_name_plural': 'ContactUs',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('notice_file', models.FileField(upload_to='Notice')),
            ],
            options={
                'verbose_name': 'Notice',
                'verbose_name_plural': 'Notices',
            },
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='TeamImage')),
                ('cover_image', models.ImageField(upload_to='TeamImage')),
                ('facebook_link', models.URLField(blank=True, max_length=500, null=True)),
                ('twitter_link', models.URLField(blank=True, max_length=500, null=True)),
                ('linkedin_link', models.URLField(blank=True, max_length=500, null=True)),
                ('instagram_link', models.URLField(blank=True, max_length=500, null=True)),
                ('ordering', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'OurTeam',
                'verbose_name_plural': 'OurTeam',
                'ordering': ['ordering'],
            },
        ),
    ]