from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Course, Degree, School, CourseType
from .forms import DegreeComparerForm

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
        pruned_courses= courses.distinct()

        matrix = [[None, *degrees]]
        for course in pruned_courses:
            row = [course]
            for degree in degrees:
                if Degree.objects.filter(id=degree.id, courses=course).exists():
                    row.append(True)
                else:
                    row.append(False)
            matrix.append(row)
        return matrix




    def post(self, request):
        form = DegreeComparerForm(request.POST)
        degrees = Degree.objects.filter(pk__in=request.POST.getlist('degrees'))
        courses = Course.objects.filter(degrees__in=degrees)
        table_data = self._build_matrix(degrees, courses)
            
        return_obj = {
            'form':form,
            'degrees': Degree.objects.all(),
            'table': table_data
        }
        return render(request, 'course_selector/degree_comparer.html', return_obj)

