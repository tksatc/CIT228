from django import forms

from .models import Task, Note

PRIORITY_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (9, '9'),
]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'due_date', 'completed', 'date_completed']
        labels = {'name': ''}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task title'}),
                   'priority': forms.Select(choices=PRIORITY_CHOICES),
                   'due_date': forms.SelectDateWidget(),
                   'completed': forms.CheckboxInput(),
                   'date_completed': forms.SelectDateWidget(),
                   }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80}),
                   'placeholder': 'Enter details or updates for the task',
                   }
