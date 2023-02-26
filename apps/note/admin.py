from django.contrib import admin
from apps.note.models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title']
