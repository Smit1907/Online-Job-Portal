# Generated by Django 4.1.5 on 2023-02-03 04:52

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_application_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='file',
            field=models.FileField(upload_to='applicant/cv/', validators=[app.validators.validate_file_extension]),
        ),
    ]
