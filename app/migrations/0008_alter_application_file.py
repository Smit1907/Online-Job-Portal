# Generated by Django 4.1.5 on 2023-02-03 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_application_file_alter_jobs_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='file',
            field=models.FileField(upload_to='applicant/cv/'),
        ),
    ]
