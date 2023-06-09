# Generated by Django 4.1.5 on 2023-02-06 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_jobs_form_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='form_start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobs',
            name='form_end_date',
            field=models.DateTimeField(),
        ),
    ]
