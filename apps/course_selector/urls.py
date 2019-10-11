from django.urls import path
from . import views

app_name = 'course_selector'

urlpatterns = [
    path('', views.index, name='index'),
    path('degree-comparison', views.DegreeComparer.as_view(), name='degree-comparer'),
    path('courses', views.CourseList.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course-detail'),
    path('degrees', views.DegreesList.as_view(), name='degrees'),
    path('degrees/<int:pk>/', views.DegreeDetail.as_view(), name='degree-detail'),

]
