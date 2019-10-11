from django.contrib import admin
from .models import Course, Degree, Certification

# Register your models here.

admin.site.register(Course)
admin.site.register(Degree)
admin.site.register(Certification)