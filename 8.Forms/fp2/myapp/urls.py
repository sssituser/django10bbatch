from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.employees),
    path('register/',views.register),
]