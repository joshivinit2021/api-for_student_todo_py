from django.urls import path
# from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.studentOverview, name="stundent-overview"),
    path('student_list/',views.student_list,name="studentlist"),
    path('student_detail/<str:pk>/',views.student_detail,name="student_detail"),
    path('student_create/',views.student_create,name="student_create"),
    path('student_update/<str:pk>/',views.student_update,name="student_update"),
    path('student_delete/<str:pk>/',views.student_delete,name="student_delete"),
]
