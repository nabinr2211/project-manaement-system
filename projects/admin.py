from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from projects.models import *


@admin.register(Program)
class Program(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Supervisor)
class Supervisor(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'position']
    list_filter = ('position',)


# @admin.register(Task)
class Task(admin.TabularInline):
    model = Task


@admin.register(Member)
class Member(admin.ModelAdmin):
    inlines = [Task,]
    list_display = ['name', 'symbol_no', 'program', 'email', 'phone', 'semester', ]

    search_fields = ('name',)
    list_filter = ('program', 'semester')


@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'members', 'supervisors']

    def supervisors(self, obj):
        return format_html('<br/>'.join([p.name for p in obj.supervisor.all()]))

    def members(self, obj):
        return format_html('<br/>'.join([p.name for p in obj.member.all()]))

    search_fields = ('title',)
    list_filter = ('title', 'supervisor')
