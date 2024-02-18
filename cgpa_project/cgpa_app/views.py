from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Student_Model, Subjects_Model, Grade_model
from .forms import *

def home(request):
   return render(request, 'home.html')

def add_student(request):
    if request.method == 'POST':
        form = student_add_form(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_list')
    else:
        form = student_add_form()
    return render(request, 'add_student.html', {'form': form})

def add_subjects(request):
    if request.method == 'POST':
        form = subjects_add_form(request.POST)
        if form.is_valid():
            subject = form.save()
            return redirect('subject_list')
    else:
        form = subjects_add_form()
    return render(request, 'add_subjects.html', {'form': form})

def student_list(request):
    students = Student_Model.objects.all()
    return render(request, 'student_list.html', {'students': students})

def subject_list(request):
    subjects = Subjects_Model.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def add_subjects_to_student(request, student_id):
    student = get_object_or_404(Student_Model, id=student_id)

    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['student_sub']  
            marks = form.cleaned_data['marks']

            Grade_model.objects.create(student=student, student_sub=subject, marks=marks)

            return redirect('student_list')
    else:
        form = GradeForm()

    return render(request, 'add_subjects_to_student.html', {'form': form, 'student': student, 'student_id': student_id})

def user_delete(request, id):
    prof=Student_Model.objects.filter(id=id)
    prof.delete()
    return redirect('student_list')













































# from django.shortcuts import render,redirect
# from .models import*
# from .forms import*
# # Create your views here.

# def home(request):
#     return render(request, 'home.html')

# def student_add(request):
#     if request.method == 'POST':
#         form = student_add_form(request.POST)
#         if form.is_valid():
#             student = form.save()

#             subjects = request.POST.getlist('subjects')
#             student.subjects.set(subjects)
#             return redirect('student_list')
#     else:
#         form = student_add_form()
#     return render(request, 'student.html',{'form':form})

# def student_list(request):
#     student = Student_Model.objects.all()
#     context={
#         'stud':student

#     }
#     return render(request, 'student_l.html', context)

# def subjects_add(request):
#     if request.method == 'POST':
#         form = subjects_add_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = subjects_add_form()
#     return render(request, 'subjects.html',{'form':form})
