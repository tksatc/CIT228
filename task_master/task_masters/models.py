from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    """A Task the user has"""

    name = models.CharField(max_length=300)
    priority = models.CharField(max_length=1)
    due_date = models.DateField(null=True)
    completed = models.BooleanField(default=False)
    date_completed = models.DateField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class Note(models.Model):
    """A note or update on the task"""
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'notes'

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.text[:50]}..."
