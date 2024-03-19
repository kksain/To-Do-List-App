from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
]
