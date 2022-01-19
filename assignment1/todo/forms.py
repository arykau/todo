from dataclasses import field
from django import forms

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'


class CreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
