from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView

from projects.decorators import unauthenticated_user, allowed_user
from projects.forms import *
from django.contrib.auth import authenticate, login, logout


# Create your views here.

@login_required(login_url=reverse_lazy('projects:user_login'))
def dashboard(request):
    projects = Project.objects.all()
    totalMember = Member.objects.all().count()
    totalProjects = Project.objects.all().count()
    totalPrograms = Program.objects.all().count()
    totalSupervisor=Supervisor.objects.all().count()
    programs=Program.objects.all()
    return render(request, 'dashboard.html',
                  {'projects': projects, 'total_member': totalMember, 'total_project': totalProjects,
                   'total_program': totalPrograms, 'total_supervisor':totalSupervisor,'programs':programs})


# views for add program example:BCA, BBA, BE computer....
@login_required(login_url=reverse_lazy('projects:user_login'))
def add_program(request):
    if request.method == "GET":
        ProgramForm = AddProgramModelsForm()
        return render(request, 'program/add_program.html', {'program_form': ProgramForm})
    elif request.method == "POST":
        form = AddProgramModelsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your Prrogram has been created!!!')
        else:
            return render(request, 'program/add_program.html', {'program_form': form})
        return redirect('projects:program_list')
    return redirect('dashboard')


"""
views for the program list 
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'program/program_list.html', {'programs': programs})


""" 
.....views for the edit program.....
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def edit_program(request, id):
    edit = Program.objects.get(id=id)
    if request.method == "GET":
        editProgram = EditProgramModelsForm(instance=edit)
        return render(request, 'program/edit_program.html', {'edit_program': editProgram})
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


@login_required(login_url=reverse_lazy('projects:user_login'))
def delete_program(request, id):
    deleteProgram = Program.objects.get(id=id)
    if request.method == "POST":
        deleteProgram.delete()
        return redirect('projects:program_list')
    return render(request, 'program/delete_program.html', {'deleteProgram': deleteProgram})


"""
views for add member ...

"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def add_member(request):
    if request.method == "GET":
        MemberForm = AddMemberModelsForm()
        # tasks = AddTaskModelsForm()
        return render(request, 'member/add_member.html', {'member_form': MemberForm})  # ,'tasks_form':tasks
    elif request.method == "POST":
        form = AddMemberModelsForm(request.POST)

        if form.is_valid():
            form.save()
            # task.save()
        else:
            return render(request, 'member/add_member.html', {'member_form': form})  # ,'tasks_form':task
        return redirect('projects:member_list')
    return redirect('dashboard')


"""
views for the  members list
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def member_list(request):
    members = Member.objects.all()
    return render(request, 'member/member_list.html', {'members': members})


""" 
.....views for the edit program.....
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def edit_member(request, id):
    edit = Member.objects.get(id=id)
    if request.method == "GET":
        editMember = EditMemberModelsForm(instance=edit)
        return render(request, 'member/edit_member.html', {'edit_member': editMember})
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


@login_required(login_url=reverse_lazy('projects:user_login'))
def delete_member(request, id):
    deleteMember = Member.objects.get(id=id)
    if request.method == "POST":
        deleteMember.delete()
        return redirect('projects:member_list')
    return render(request, 'member/delete_member.html', {'deleteMember': deleteMember})


"""
views for add member ...

"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def add_supervisor(request):
    if request.method == "GET":
        SupervisorForm = AddSupervisorModelsForm()
        return render(request, 'supervisor/add_supervisor.html', {'supervisor_form': SupervisorForm})
    elif request.method == "POST":
        form = AddSupervisorModelsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'supervisor/add_supervisor.html', {'supervisor_form': form})
        return redirect('projects:supervisor_list')
    return redirect('dashboard')


"""
views for the  members list
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def supervisor_list(request):
    supervisors = Supervisor.objects.all()
    return render(request, 'supervisor/supervisor_list.html', {'supervisors': supervisors})


"""
.....views for the edit supervisor.....
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def edit_supervisor(request, id):
    edit = Supervisor.objects.get(id=id)
    if request.method == "GET":
        editSupervisor = EditSupervisorModelsForm(instance=edit)
        return render(request, 'supervisor/edit_supervisor.html', {'edit_supervisor': editSupervisor})
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


@login_required(login_url=reverse_lazy('projects:user_login'))
def delete_supervisor(request, id):
    deleteSupervisor = Supervisor.objects.get(id=id)
    if request.method == "POST":
        deleteSupervisor.delete()
        return redirect('projects:supervisor_list')
    return render(request, 'supervisor/delete_supervisor.html', {'delete_supervisor': deleteSupervisor})


"""
views for add task ...
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def add_task(request):
    if request.method == "GET":
        TaskForm = AddTaskModelsForm()
        return render(request, 'task/add_task.html', {'task_form': TaskForm})
    elif request.method == "POST":
        form = AddTaskModelsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'task/add_task.html', {'task_form': form})
        return redirect('projects:task_list')
    return redirect('projects:task_list')


"""
views for the  task list
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def task_list(request):
    task = Task.objects.all()
    return render(request, 'task/task_list.html', {'task': task})


"""
.....views for the edit task.....
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def edit_task(request, id):
    edit = Task.objects.get(id=id)
    if request.method == "GET":
        editTask = EditTaskModelsForm(instance=edit)
        return render(request, 'task/edit_task.html', {'edit_task': editTask})
    elif request.method == "POST":
        edit_task = EditTaskModelsForm(request.POST, instance=edit)
        if edit_task.is_valid():
            edit_task.save()
        else:
            return redirect('projects:task_list')
        return redirect('projects:task_list')


"""
....views for delete task....
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def delete_task(request, id):
    deleteTask = Task.objects.get(id=id)
    if request.method == "POST":
        deleteTask.delete()
        return redirect('projects:task_list')
    return render(request, 'task/delete_task.html', {'delete_task': deleteTask})


"""
views for add Projects ...
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def add_project(request):
    if request.method == "GET":
        ProjectForm = AddProjectModelsForm()

        return render(request, 'projects/add_project.html', {'project_form': ProjectForm})
    elif request.method == "POST":
        form = AddProjectModelsForm(request.POST)

        if form.is_valid():
            form.save()

        else:
            return render(request, 'projects/add_project.html', {'project_form': form})
        return redirect('projects:project_list')
    return redirect('projects:project_list')


"""
views for the  task list
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


"""
.....views for the edit task.....
"""


@login_required(login_url=reverse_lazy('projects:user_login'))
def edit_project(request, id):
    edit = Project.objects.get(id=id)
    if request.method == "GET":
        editProject = EditProjectModelsForm(instance=edit)
        return render(request, 'projects/edit_project.html', {'edit_project': editProject})
    elif request.method == "POST":
        edit_project = EditProjectModelsForm(request.POST, instance=edit)
        if edit_project.is_valid():
            edit_project.save()
        else:
            return redirect('projects:project_list')
        return redirect('projects:project_list')


"""
....views for delete project....
"""


def delete_project(request, id):
    deleteProject = Project.objects.get(id=id)
    if request.method == "POST":
        deleteProject.delete()
        return redirect('projects:project_list')
    return render(request, 'projects/delete_project.html', {'delete_projects': deleteProject})


class ProjectDetails(DetailView):
    model = Project
    query_pk_and_slug = True
    slug_field = 'title'
    template_name = 'projects/project_detail.html'


@unauthenticated_user
def user_login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('projects:user_login')

        else:
            return redirect('projects:user_login')


def user_logout(request):
    logout(request)
    return redirect("projects:user_login")
