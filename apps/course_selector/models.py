from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Course(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.CharField(blank=False, max_length=10000)
    prereqs = models.ManyToManyField('self', blank=True, null=True)
    comp_units = models.IntegerField(
        default=3,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ]
    )

    def __str__(self):
        return self.name

class Degree(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.CharField(blank=False, max_length=10000)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name