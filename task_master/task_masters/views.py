from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Task, Note
from .forms import TaskForm, NoteForm


# Create your views here.
def index(request):
    """Home page for Task Master"""
    return render(request, 'task_masters/index.html')


@login_required
def tasks(request):
    """Show all tasks"""
    tasks = Task.objects.filter(owner=request.user).order_by('due_date')
    context = {'tasks': tasks}
    return render(request, 'task_masters/tasks.html', context)


@login_required
def task(request, task_id):
    """Show a single task and all its notes"""
    task = Task.objects.get(id=task_id)
    # Make sure the task belongs to the current user
    if task.owner != request.user:
        raise Http404

    notes = task.note_set.order_by('-date_added')
    context = {'task': task, 'notes': notes}
    return render(request, 'task_masters/task.html', context)


@login_required
def new_task(request):
    """Create a new task"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TaskForm()
    else:
        # POST data submitted; process data
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('task_masters:tasks')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'task_masters/new_task.html', context)


@login_required
def new_note(request, task_id):
    """Add a new note for a specific task"""
    task = Task.objects.get(id=task_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = NoteForm()
    else:
        # POST data submitted; process data
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.task = task
            new_note.save()
            return redirect('task_masters:task', task_id=task_id)

    # Display a blank or invalid form
    context = {'task': task, 'form': form}
    return render(request, 'task_masters/new_note.html', context)


@login_required
def edit_task(request, task_id):
    """Edit task to mark commplete"""
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_masters:task', task_id=task.id)

    context = {'task': task, 'form': form}
    return render(request, 'task_masters/edit_task.html', context)


@login_required
def edit_note(request, note_id):
    """Edit an existing note"""
    note = Note.objects.get(id=note_id)
    task = note.task
    if task.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry
        form = NoteForm(instance=note)
    else:
        # POST data submitted; process data
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_masters:task', task_id=task.id)

    context = {'note': note, 'task': task, 'form': form}
    return render(request, 'task_masters/edit_note.html', context)
