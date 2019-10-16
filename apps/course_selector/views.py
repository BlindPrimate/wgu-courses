from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Course, Degree
from .forms import DegreeComparerForm

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

class DegreeComparer(FormView):
    template_name = 'course_selector/degree_comparer.html'
    form_class = DegreeComparerForm

    def post(self, request):
        form = DegreeComparerForm(request.POST)
        return_obj = {
            'form':form,
            'degrees': Degree.objects.all(),
            'courses': Course.objects.all()
        }
        return render(request, 'course_selector/degree_comparer.html', return_obj)

