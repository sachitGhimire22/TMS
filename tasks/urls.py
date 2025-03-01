from django.urls import path
from . import views  # Correct way to import views.py from the same directory
from .views import task_create


urlpatterns = [
    path('', views.tasks_list, name='tasks_list'),  # This should work now
    path('create/', task_create, name='task_create')
]
