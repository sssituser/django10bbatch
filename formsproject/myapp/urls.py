from django.urls import path
from myapp import views
urlpatterns=[
    path('',views.getstudents),
    path('add/',views.register),
]