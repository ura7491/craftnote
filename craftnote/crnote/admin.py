from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('Дата_создания',)

admin.site.register(Task, TaskAdmin)