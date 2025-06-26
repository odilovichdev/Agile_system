from django.contrib import admin

from .models import Task, TaskHistory


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    pass


@admin.register(TaskHistory)
class TaskHistoryModelAdmin(admin.ModelAdmin):
    pass
