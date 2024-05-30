from django.shortcuts import render, redirect
from .models import Student, Course, StudentGrade
from .forms import StudentForm, CourseForm, StudentGradeForm

def home(request):
  return render(request, 'grades/home.html')

def create_student(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = StudentForm()
  return render(request, 'grades/create_student.html', {'form': form})

def create_course(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = CourseForm()
  return render(request, 'grades/create_course.html', {'form': form})

def create_student_grade(request):
  if request.method == 'POST':
    form = StudentGradeForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = StudentGradeForm()
  return render(request, 'grades/create_student_grade.html', {'form': form})

def list_student_grades(request):
    grades = StudentGrade.objects.select_related('student', 'course').all()
    return render(request, 'grades/list_student_grades.html', {'grades': grades})
