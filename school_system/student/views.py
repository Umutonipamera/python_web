from django.shortcuts import render
from .forms import StudentRegistrationForm
# Create your views here.

def register_student(request):
    form = StudentRegistrationForm()
    return render(request,"register-student.html",{"form":form})
