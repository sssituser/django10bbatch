from django.shortcuts import render,redirect
from myapp.forms import EmployeeForm
from myapp.models import Employee
# Create your views here.
def register(request):
    form  = EmployeeForm()
    if request.method=="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    return render(request,'myapp/register.html',{"rform":form})

def employees(request):
    emps =Employee.objects.all()
    return render(request,'myapp/employees.html',{'emplist':emps})
