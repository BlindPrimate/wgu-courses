from django.db import models 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Certification(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.CharField(blank=True, max_length=10000)
    link = models.URLField(default="http://www.wgu.edu")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(blank=False, max_length=255)
    course_number = models.CharField(blank=False, default="C", max_length=4)
    description = models.TextField(blank=False, max_length=10000)
    prereqs = models.ManyToManyField('self', blank=True, verbose_name="Prerequisites")
    certificate_earned = models.ForeignKey(Certification, blank=True, null=True, on_delete=models.PROTECT)
    comp_units = models.IntegerField(
        'Competency Units',
        default=3,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ]
    )
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.course_number + " " + self.name



class Degree(models.Model):
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False, max_length=10000)
    courses = models.ManyToManyField(Course, related_name="degrees")
    earned_certifications = models.ManyToManyField(Certification, blank=True)
    link = models.URLField(blank=False, default="http://www.wgu.edu", max_length=200)
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