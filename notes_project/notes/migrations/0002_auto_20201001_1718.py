# Generated by Django 3.1.2 on 2020-10-01 17:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='notes_description',
            new_name='note_description',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='notes_title',
            new_name='note_title',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='notes_type',
            new_name='note_type',
        ),
    ]
