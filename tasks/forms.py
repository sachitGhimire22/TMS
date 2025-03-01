from django import forms
from .models import tasks

class TaskForm(forms.ModelForm):
    class Meta:
        model = tasks
        fields = '__all__' # This will include all fields in the form