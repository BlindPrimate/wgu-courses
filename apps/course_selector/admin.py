from django.contrib import admin
from .models import Course, Degree, Certification, School

# Register your models here.

admin.site.register(Course)
admin.site.register(Degree)
admin.site.register(Certification)
admin.site.register(School)