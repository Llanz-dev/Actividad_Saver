from django.contrib import admin
from lists.models import Tasks

class TasksAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Tasks, TasksAdmin)
