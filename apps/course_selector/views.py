from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Course, Degree, School, CourseType
from .forms import DegreeComparerForm
from django.db.models import Count
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

class CourseList(TemplateView):
    def get(self, request, **kwargs):
        courses = Course.objects.all()
        course_types = CourseType.objects.all()
        context = {
            "all_courses": courses,
            "categorized": course_types,
            "uncategorized": courses.filter(course_type__isnull=True)
        }
        return render(request, template_name='course_selector/course_list.html', context=context)

class DegreesList(TemplateView):
    def get(self, request, **kwargs):
        context = {}
        context['categorized'] = School.objects.all()
        context['degrees'] =  Degree.objects.all()
        return render(request, template_name='course_selector/degree_list.html', context=context)

class DegreeComparer(FormView):
    template_name = 'course_selector/degree_comparer.html'
    form_class = DegreeComparerForm

    def _build_table(self, degrees, courses):
        '''
        Builds the matrix for constructing the degree comparer table
        ''' 

        pruned_courses = courses.distinct()
        course_type_list = pruned_courses.values('course_type').distinct()
        course_types = CourseType.objects.filter(courses__in=course_type_list).select_related()

        table = {
            "header": [None, *degrees],
            "body": []
        }

        for course_type in course_types:
            table['body'].append({
                "name": course_type,
            })
            for course in course_type.courses.all():
                table_entry_obj = {
                    "name": course.name,
                    "entry": [],
                }
                for degree in degrees:
                    if course in degree.courses.all():
                        table_entry_obj['entry'].append(True)
                    else:
                        table_entry_obj['entry'].append(False)
                table['body'].append(table_entry_obj)
        pp.pprint(table)
        return table




    def post(self, request):
        form = DegreeComparerForm(request.POST)
        degrees = Degree.objects.all()
        queried_degrees = degrees.filter(pk__in=request.POST.getlist('degrees'))
        courses = Course.objects.filter(degrees__in=queried_degrees)
        table_data = self._build_table(queried_degrees, courses)
            
        return_obj = {
            'form':form,
            'degrees': degrees,
            'table': table_data,
        }
        return render(request, 'course_selector/degree_comparer.html', return_obj)

