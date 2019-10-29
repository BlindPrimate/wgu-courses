from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, TemplateView
from .models import Course, Degree, School, CourseType, Certification
from .forms import DegreeComparerForm
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

    def _build_table_certs(self, degrees):
        certs = Certification.objects.filter(degrees__in=degrees).distinct()
        table = {
            "title": 'Certifications',
            "body": []
        }
        for cert in certs:
            row = [cert]
            for degree in degrees:
                if degree in cert.degrees.all():
                    row.append(True)
                else:
                    row.append(False)

            table['body'].append(row)

        return table

    def _build_course_table(self, courses, degrees, course_type):
        table = {
            "name": course_type,
            "body": []
        }
        for course in course_type.courses.filter(id__in=courses):
            row = [course]
            for degree in degrees:
                if course in degree.courses.all():
                    row.append(True)
                else:
                    row.append(False)
            table['body'].append(row)
        return table


    def _build_table_courses(self, degrees, courses):
        '''
        Builds the courses table for constructing the degree comparer
        ''' 

        course_type_list = courses.values('course_type').distinct()
        course_types = CourseType.objects.filter(courses__in=course_type_list).select_related()

        tables = []
        for course_type in course_types:
            table = self._build_course_table(courses, degrees, course_type)
            tables.append(table)

        return tables

        # pp.pprint([self._build_course_table(courses, degrees, x) for x in course_types])

        # for course_type in course_types:
        #     table['body'].append({
        #         "name": course_type,
        #     })
        #     for course in course_type.courses.filter(id__in=pruned_courses):
        #         table_entry_obj = {
        #             "name": course.name,
        #             "entry": [],
        #         }
        #         for degree in degrees:
        #             if course in degree.courses.all():
        #                 table_entry_obj['entry'].append(True)
        #             else:
        #                 table_entry_obj['entry'].append(False)
        #         table['body'].append(table_entry_obj)
        
        # pp.pprint(table)
        # return table

    def post(self, request):
        form = DegreeComparerForm(request.POST)
        degrees = Degree.objects.all()
        queried_degrees = degrees.filter(pk__in=request.POST.getlist('degrees'))
        courses = Course.objects.filter(degrees__in=queried_degrees).distinct()
            
        return_obj = {
            'form':form,
            'degrees': degrees,
            'table_header': [None, *[degree for degree in queried_degrees.all()]],
            'table_courses': self._build_table_courses(queried_degrees, courses),
            'table_certs': self._build_table_certs(queried_degrees),
        }
        # pp.pprint(return_obj['table_header'][1].name)
        # pp.pprint(return_obj['table_header'])
        # pp.pprint(return_obj['table_courses'])
        pp.pprint(return_obj)
        return render(request, 'course_selector/degree_comparer.html', return_obj)

