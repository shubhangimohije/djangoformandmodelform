from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm, UniversityForm
# Create your views here.
def dispaly(request):
    return HttpResponse('this is model form view')

def view_student(request):
    student=StudentForm()
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            # process form data
            obj = Student()  # gets new object
            obj.sid = student.cleaned_data['sid']
            obj.name = student.cleaned_data['name']
            obj.email = student.cleaned_data['email']
            obj.save()
            return redirect('stu')
    return render(request,'student.html',{'form':student})

def view_university(request):
    uni=UniversityForm()
    if (request.method == 'POST'):
        uni=UniversityForm(request.POST)
        if (uni.is_valid()):
            uni.save()
        return redirect('uni')
    return render(request,'uni.html',{'form':uni})

