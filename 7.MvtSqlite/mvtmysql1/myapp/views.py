from django.shortcuts import render
from myapp.models import Customer
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    return render(request,'myapp/home.html',{'cust_list':customers})
