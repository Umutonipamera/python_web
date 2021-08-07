from django.shortcuts import render
from .forms import StudentRegistrationForm
# Create your views here.

def register_student(request):
    form = StudentRegistrationForm()
    return render(request,"register-student.html",{"form":form})

def register_student(request):
    if request.method == "POST":
        form=StudentRegistrationForm(request.POST)
        if form .is_valid():
            form.save()
        else:
            print(form.errors)
    else:
            form=StudentRegistrationForm()
    return render(request,'register-student.html',{"form":form})

