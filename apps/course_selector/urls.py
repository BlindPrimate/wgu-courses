from django.urls import path, re_path
from . import views

app_name = 'course_selector'

urlpatterns = [
    path('', views.index, name='index'),
    path('degree-comparison', views.DegreeComparer.as_view(), name='degree-comparer'),
    path('courses', views.CourseList.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseList.as_view()),
    path('degrees', views.DegreesList.as_view(), name='degrees'),
    path('degrees/<int:pk>/', views.DegreesList.as_view()),
]
