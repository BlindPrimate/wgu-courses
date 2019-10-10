from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Course(models.Model):
    course_number = models.CharField(blank=False, default=1, max_length=4)
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False, max_length=10000)
    prereqs = models.ManyToManyField('self', blank=True)
    comp_units = models.IntegerField(
        default=3,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ]
    )
    class Meta:
        ordering = ['course_number']

    def __str__(self):
        return self.course_number + " " + self.name
        # return self.name

class Degree(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.CharField(blank=False, max_length=10000)
    courses = models.ManyToManyField(Course)
    degree_type = models.CharField(
        max_length=4,
        default="B.S.",
        choices=[
            ("B.S.", "Bachelors of Science"),
            ("M.S.", "Masters of Science")
        ]
    )

    def __str__(self):
        return self.degree_type + " " + self.name
        # return self.name