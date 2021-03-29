from django.shortcuts import render, redirect
from django.contrib import messages

from projects.forms import *


# Create your views here.
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'dashboard.html', {'projects': projects})


# views for add program example:BCA, BBA, BE computer....
def add_program(request):
    if request.method == "GET":
        ProgramForm = AddProgramModelsForm()
        return render(request, 'add_program.html', {'program_form': ProgramForm})
    elif request.method == "POST":
        form = AddProgramModelsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Prrogram has been created!!!')
        else:
            return render(request, 'add_program.html', {'program_form': form})
        return redirect('projects:program_list')
    return redirect('dashboard')


"""
views for the program list 
"""


def program_list(request):
    programs = Program.objects.all()
    return render(request, 'program_list.html', {'programs': programs})


""" 
.....views for the edit program.....
"""


def edit_program(request, id):
    edit = Program.objects.get(id=id)
    if request.method == "GET":
        editProgram = EditProgramModelsForm(instance=edit)
        return render(request, 'edit_program.html', {'edit_program': editProgram})
    elif request.method == "POST":
        edit_program = EditProgramModelsForm(request.POST, instance=edit)
        if edit_program.is_valid():
            edit_program.save()
        else:
            return redirect('projects:program_list')
        return redirect('projects:program_list')


"""
....views for delete program....
"""


def delete_program(request, id):
    deleteProgram = Program.objects.get(id=id)
    if request.method == "POST":
        deleteProgram.delete()
        return redirect('projects:program_list')
    return render(request, 'delete_program.html', {'deleteProgram': deleteProgram})


"""
views for add member ...

"""


def add_member(request):
    if request.method == "GET":
        MemberForm = AddMemberModelsForm()
        return render(request, 'add_member.html', {'member_form': MemberForm})
    elif request.method == "POST":
        form = AddMemberModelsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'add_member.html', {'member_form': form})
        return redirect('projects:member_list')
    return redirect('dashboard')


"""
views for the  members list
"""


def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})


""" 
.....views for the edit program.....
"""


def edit_member(request, id):
    edit = Member.objects.get(id=id)
    if request.method == "GET":
        editMember = EditMemberModelsForm(instance=edit)
        return render(request, 'edit_member.html', {'edit_member': editMember})
    elif request.method == "POST":
        edit_member = EditMemberModelsForm(request.POST, instance=edit)
        if edit_member.is_valid():
            edit_member.save()
        else:
            return redirect('projects:member_list')
        return redirect('projects:member_list')


"""
....views for delete program....
"""


def delete_member(request, id):
    deleteMember = Member.objects.get(id=id)
    if request.method == "POST":
        deleteMember.delete()
        return redirect('projects:member_list')
    return render(request, 'delete_member.html', {'deleteMember': deleteMember})


"""
views for add member ...

"""


def add_supervisor(request):
    if request.method == "GET":
        SupervisorForm = AddSupervisorModelsForm()
        return render(request, 'add_supervisor.html', {'supervisor_form': SupervisorForm})
    elif request.method == "POST":
        form = AddSupervisorModelsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'add_supervisor.html', {'supervisor_form': form})
        return redirect('projects:supervisor_list')
    return redirect('dashboard')


"""
views for the  members list
"""


def supervisor_list(request):
    supervisors = Supervisor.objects.all()
    return render(request, 'supervisor_list.html', {'supervisors': supervisors})


"""
.....views for the edit supervisor.....
"""


def edit_supervisor(request, id):
    edit = Supervisor.objects.get(id=id)
    if request.method == "GET":
        editSupervisor = EditSupervisorModelsForm(instance=edit)
        return render(request, 'edit_supervisor.html', {'edit_supervisor': editSupervisor})
    elif request.method == "POST":
        edit_supervisor = EditSupervisorModelsForm(request.POST, instance=edit)
        if edit_supervisor.is_valid():
            edit_supervisor.save()
        else:
            return redirect('projects:supervisor_list')
        return redirect('projects:supervisor_list')


"""
....views for delete supervisor....
"""


def delete_supervisor(request, id):
    deleteSupervisor = Supervisor.objects.get(id=id)
    if request.method == "POST":
        deleteSupervisor.delete()
        return redirect('projects:delete_supervisor')
    return render(request, 'delete_supervisor.html', {'delete_supervisor': deleteSupervisor})


"""
views for add task ...

"""


def add_task(request):
    if request.method == "GET":
        TaskForm = AddTaskModelsForm()
        return render(request, 'add_task.html', {'task_form': TaskForm})
    elif request.method == "POST":
        form = AddTaskModelsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'add_task.html', {'task_form': form})
        return redirect('dashboard')
    return redirect('dashboard')


"""
views for the  task list
"""


def task_list(request):
    task = Task.objects.all()
    return render(request, 'task_list.html', {'task': task})


"""
.....views for the edit supervisor.....
"""


def edit_supervisor(request, id):
    edit = Supervisor.objects.get(id=id)
    if request.method == "GET":
        editSupervisor = EditSupervisorModelsForm(instance=edit)
        return render(request, 'edit_supervisor.html', {'edit_supervisor': editSupervisor})
    elif request.method == "POST":
        edit_supervisor = EditSupervisorModelsForm(request.POST, instance=edit)
        if edit_supervisor.is_valid():
            edit_supervisor.save()
        else:
            return redirect('projects:supervisor_list')
        return redirect('projects:supervisor_list')


"""
....views for delete supervisor....
"""


def delete_supervisor(request, id):
    deleteSupervisor = Supervisor.objects.get(id=id)
    if request.method == "POST":
        deleteSupervisor.delete()
        return redirect('projects:delete_supervisor')
    return render(request, 'delete_supervisor.html', {'delete_supervisor': deleteSupervisor})



