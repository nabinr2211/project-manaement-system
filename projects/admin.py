from django.contrib import admin

# Register your models here.
from projects.models import *


@admin.register(Program)
class Program(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Supervisor)
class Supervisor(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Member)
class Member(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ['title']
