from django.shortcuts import render,redirect
from myapp.forms import EmployoeeForm
from myapp.models import Employee
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')

def register(request):
    form = EmployoeeForm()
    if request.method == 'POST':
        form = EmployoeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/employees')
    return render(request,'myapp/register.html',{'rform':form})

def edit(request):
    return render(request,'myapp/edit.html')

def details(request):
    return render(request,'myapp/details.html')

def delete(request):
    return (request,'myapp/delete.html')

def employees(request):
    emps = Employee.objects.all()
    return render(request,'myapp/employees.html',{'emps':emps})



