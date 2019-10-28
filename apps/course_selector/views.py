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

    def _build_matrix(self, degrees, courses):
        '''
        Builds the matrix for constructing the degree comparer table
        ''' 
        pruned_courses = courses.distinct().order_by('course_type')
        course_types = pruned_courses.values('course_type').distinct().annotate(name_count=Count('course_type'))

        matrix = [[None, *degrees]]
        for course_type in course_types:
            print(course_type)
            matrix.append([course_type])
            for course in pruned_courses:
                row = []
                if course.course_type.id == course_type['course_type'] and len(row) < 1:
                    row.append(course)
                    for degree in degrees:
                        if course in degree.courses.all():
                            row.append(True)
                        else:
                            row.append(False)
                    matrix.append(row)

        # pp.pprint(matrix)
        return matrix




    def post(self, request):
        form = DegreeComparerForm(request.POST)
        degrees = Degree.objects.all()
        queried_degrees = degrees.filter(pk__in=request.POST.getlist('degrees'))
        courses = Course.objects.filter(degrees__in=queried_degrees)
        table_data = self._build_matrix(queried_degrees, courses)
            
        return_obj = {
            'form':form,
            'degrees': Degree.objects.all(),
            'table': table_data
        }
        return render(request, 'course_selector/degree_comparer.html', return_obj)

