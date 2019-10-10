# Generated by Django 2.2.6 on 2019-10-10 03:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_number', models.CharField(default=1, max_length=4)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=10000)),
                ('comp_units', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('prereqs', models.ManyToManyField(blank=True, related_name='_course_prereqs_+', to='course_selector.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=10000)),
                ('degree_type', models.CharField(choices=[('Bachelors of Science', 'B.S.'), ('Masters of Science', 'M.S.')], default='B.S.', max_length=2)),
                ('courses', models.ManyToManyField(to='course_selector.Course')),
            ],
        ),
    ]
