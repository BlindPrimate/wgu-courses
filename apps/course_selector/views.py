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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['knock'] = "knock"
        return context

class DegreesList(ListView):
    context_object_name = 'degrees'
    template_name = 'course_selector/degree_list.html'
    model = Degree

class DegreeComparer(ListView):
    template_name = 'course_selector/degree_comparer.html'
    model = Degree
