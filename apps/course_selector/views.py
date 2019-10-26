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

class DegreesList(ListView):
    context_object_name = 'degrees'
    template_name = 'course_selector/degree_list.html'
    model = Degree

class DegreeComparer(FormView):
    template_name = 'course_selector/degree_comparer.html'
    form_class = DegreeComparerForm

    def build_matrix(self, degrees, courses):
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
        table_data = self.build_matrix(degrees, courses)
            
        return_obj = {
            'form':form,
            'degrees': Degree.objects.all(),
            'table': table_data
        }
        return render(request, 'course_selector/degree_comparer.html', return_obj)

