from django.shortcuts import render
from myapp.models import Student
# Create your views here.
def home(request):
    stud_list = Student.objects.all()
    return render(request,'myapp/home.html',{"studs":stud_list})
