from django.contrib import admin
from .models import Course, Degree, Certification, School, CourseType


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ['name', 'school', 'degree_type']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'course_number',
        'comp_units', 
        'course_type', 
        'certificate_earned'
    ]
    search_fields = ['name']

# Register your models here.
admin.site.register(CourseType)
admin.site.register(Certification)
admin.site.register(School)