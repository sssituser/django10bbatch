from django.urls import path
from myapp import views

urlpatterns =[
    path('',views.home),
    path('register/',views.register),
    path('employees/',views.employees,name='emplist'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('edit/',views.edit),
    path('delete/',views.delete),
    path('detials/',views.details),
]