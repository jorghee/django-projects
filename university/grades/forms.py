from django import forms
from .models import Student, Course, StudentGrade

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['first_name', 'last_name', 'email']

class CourseForm(forms.ModelForm):
  class Meta:
    model = Course
    fields = ['name', 'code']

class StudentGradeForm(forms.ModelForm):
  class Meta:
    model = StudentGrade
    fields = ['student', 'course', 'grade']
