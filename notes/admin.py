from django.contrib import admin

from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_create', 'date_update', )


admin.site.register(Note, NoteAdmin)
