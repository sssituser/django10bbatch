from django.shortcuts import render
from myapp.models import Employee
# Create your views here.
def home(request):
    emp_list=Employee.objects.all()
    return render(request,'myapp/home.html',{"emps":emp_list})
