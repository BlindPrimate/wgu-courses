from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course, Degree

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

class CourseList(ListView):
    context_object_name = 'courses'
    template_name = 'course_selector/course_list.html'
    model = Course

class DegreesList(ListView):
    context_object_name = 'degrees'
    template_name = 'course_selector/degree_list.html'
    model = Degree

class DegreeComparer(ListView):
    template_name = 'course_selector/degree_comparer.html'
    model = Degree

class DegreeDetail(DetailView):
    context_object_name = 'degree'
    template_name = 'course_selector/degree_detail.html'
    model = Degree

class CourseDetail(DetailView):
    context_object_name = 'course'
    template_name = 'course_selector/course_detail.html'
    model = Course