from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):

    NOTES_CATEGORIES = (
        ('R', 'Random'),
        ('N', 'Not Important'),
        ('M', 'Most Important'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_type = models.CharField(max_length=30, choices=NOTES_CATEGORIES)
    note_title = models.CharField(max_length=100)
    note_description = models.CharField(max_length=1000)
