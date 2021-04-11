"""Defines URL patterns for task_masters"""

from django.urls import path
from . import views

app_name = 'task_masters'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all tasks
    path('tasks/', views.tasks, name='tasks'),
    # Detail page for a single task
    path('tasks/<int:task_id>/', views.task, name='task'),
    # Page for adding a new task
    path('new_task/', views.new_task, name="new_task"),
    # Page for adding a new note
    path('new_note/<int:task_id>/', views.new_note, name='new_note'),
    # Page for editing a note
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    # Page for editing a task
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
]
