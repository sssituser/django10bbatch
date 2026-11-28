from django.shortcuts import render,redirect
from myapp.models import Student
from myapp.forms import StudentForm
# Create your views here.
def register(request):
    form = StudentForm()
    if request.method=="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
    return render(request,'myapp/register.html',{'form':form})
def getstudents(requests):
    students = Student.objects.all()
    return render(requests,'myapp/students.html',{'students':students})
