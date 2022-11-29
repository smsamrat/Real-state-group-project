# Generated by Django 4.1.2 on 2022-11-23 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0075_feedback_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name_plural': 'Area'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name_plural': 'Districts'},
        ),
        migrations.AlterModelOptions(
            name='division',
            options={'verbose_name_plural': 'Divisions'},
        ),
        migrations.RenameField(
            model_name='district',
            old_name='country',
            new_name='division',
        ),
        migrations.RenameField(
            model_name='propertypost',
            old_name='select_district',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='propertypost',
            old_name='select_division',
            new_name='division',
        ),
        migrations.RenameField(
            model_name='propertypost',
            old_name='select_project_type',
            new_name='project_type_filter',
        ),
        migrations.RenameField(
            model_name='propertypost',
            old_name='select_property_type',
            new_name='property_type_filter',
        ),
        migrations.RemoveField(
            model_name='area',
            name='city',
        ),
        migrations.RemoveField(
            model_name='area',
            name='name',
        ),
        migrations.AddField(
            model_name='area',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indexApp.district'),
        ),
        migrations.AddField(
            model_name='area',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indexApp.division'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='division',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='propertypost',
            name='post_type',
            field=models.ManyToManyField(blank=True, null=True, related_name='pro_type', to='indexApp.property_type'),
        ),
        migrations.CreateModel(
            name='SubDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexApp.district')),
            ],
            options={
                'verbose_name_plural': 'Sub District',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='sub_district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indexApp.subdistrict'),
        ),
        migrations.AddField(
            model_name='propertypost',
            name='sub_district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indexApp.subdistrict'),
        ),
    ]
