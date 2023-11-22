from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'club2', 'fecha', 'golesclub','golesclub2' ,'important']

