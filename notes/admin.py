from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title','notes',)

admin.site.register(models.Notes, NotesAdmin)
