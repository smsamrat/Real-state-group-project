# Generated by Django 4.1.2 on 2022-10-18 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0005_alter_agent_fax_alter_agent_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_img', models.ImageField(blank=True, null=True, upload_to='gallery/office/')),
                ('project_img', models.ImageField(blank=True, null=True, upload_to='gallery/project/')),
                ('client_img', models.ImageField(blank=True, null=True, upload_to='gallery/client/')),
            ],
        ),
    ]