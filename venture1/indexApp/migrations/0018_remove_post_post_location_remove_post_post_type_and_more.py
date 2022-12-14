# Generated by Django 4.1.2 on 2022-10-27 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0017_remove_post_post_location_post_post_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_location',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
        migrations.AddField(
            model_name='post',
            name='post_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='indexApp.location'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.ManyToManyField(choices=[('feature', 'feature'), ('apartment', 'apartment'), ('land', 'land'), ('recent', 'recent')], to='indexApp.post'),
        ),
    ]
