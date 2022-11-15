from django.urls import path
# from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('tasklist/',views.tasklist,name="task-list"),
    path('task-detail/<str:pk>/',views.taskDetail,name="task-details"),
    path('task-create/',views.taskCreate,name="task-Create"),
    path('task-update/<str:pk>/',views.taskUpdate,name="task-Update"),
    path('task-delete/<str:pk>/',views.taskDelete,name="task-Delete"),
]
