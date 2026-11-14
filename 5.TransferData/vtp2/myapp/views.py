from django.shortcuts import render

# Create your views here.
def home(request):
    emp_list=[
        {
            "eid":111,
            "ename":"abc",
            "esal":50000
        },
        {
            "eid":112,
            "ename":"kiran",
            "esal":60000
        },
        {
            "eid":113,
            "ename":"Raj",
            "esal":70000
        }
    ]
    return render(request,'myapp/home.html',{"employees":emp_list})
