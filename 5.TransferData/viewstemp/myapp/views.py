from django.shortcuts import render

# Create your views here.
def home(request):
    emp={
        "eid":111,
        "ename":"kiran",
        "esal":50000
    }
    return render(request,'myapp/home.html',emp)
def register(request):
    student={
        "sid":1234,
        "sname":"Ravi",
        "smarks":500
    }
    return render(request,'myapp/register.html',student)