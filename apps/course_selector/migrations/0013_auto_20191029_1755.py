# Generated by Django 2.2.6 on 2019-10-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_selector', '0012_auto_20191029_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetype',
            name='course_type',
            field=models.CharField(max_length=50),
        ),
    ]
