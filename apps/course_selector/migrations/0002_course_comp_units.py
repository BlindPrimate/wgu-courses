# Generated by Django 2.2.6 on 2019-10-09 21:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_selector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='comp_units',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
