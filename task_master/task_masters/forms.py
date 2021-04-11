from django import forms

from .models import Task, Note

# 'priority' needs to change to forms.Select when drop-down menu is identified

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'due_date']
        labels = {'name': ''}
        widgets = {'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Task title'}),
                   'priority': forms.TextInput(attrs={'class': 'form-control'}),
                   'due_date': forms.DateInput(attrs={'class': 'form-control'}),
                   'completed': forms.CheckboxInput(attrs={'class': 'form-control'}),
                   'date_completed': forms.DateInput(attrs={'class': 'form-control'}),
                   }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80}),
                   'placeholder': 'Enter details or updates for the task',
                   }
