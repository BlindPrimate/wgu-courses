# Generated by Django 2.2.6 on 2019-10-11 03:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('course_number', models.CharField(default='C', max_length=4)),
                ('description', models.TextField(max_length=10000)),
                ('comp_units', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Competency Units')),
                ('certificate_on_completion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='certification', to='course_selector.Certification')),
                ('prereqs', models.ManyToManyField(blank=True, related_name='_course_prereqs_+', to='course_selector.Course', verbose_name='Prerequisites')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=10000)),
                ('link', models.URLField(default='http://www.wgu.edu')),
                ('degree_type', models.CharField(choices=[('B.S.', 'Bachelors of Science'), ('M.S.', 'Masters of Science')], default='B.S.', max_length=4)),
                ('courses', models.ManyToManyField(to='course_selector.Course')),
                ('earned_certifications', models.ManyToManyField(blank=True, to='course_selector.Certification')),
            ],
        ),
    ]
