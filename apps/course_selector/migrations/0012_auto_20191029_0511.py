# Generated by Django 2.2.6 on 2019-10-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_selector', '0011_auto_20191028_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='earned_certifications',
            field=models.ManyToManyField(blank=True, related_name='degrees', to='course_selector.Certification'),
        ),
    ]
