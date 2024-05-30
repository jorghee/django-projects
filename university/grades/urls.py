from django.urls import path
from .views import home, create_student, create_course, create_student_grade, list_student_grades

urlpatterns = [
  path('', home, name='home'),
  path('create-student/', create_student, name='create_student'),
  path('create-course/', create_course, name='create_course'),
  path('create-student-grade/', create_student_grade, name='create_student_grade'),
  path('list_student_grades/', list_student_grades, name='list_student_grades'),
]
