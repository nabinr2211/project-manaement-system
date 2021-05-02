from django.shortcuts import render
from rest_framework import status

from api.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from projects.models import Program, Member


# Create your views here.
@api_view(['GET', 'POST'])
def program_add_api(request):
    """
    API view function for add program....
    """
    serializer = ProgramSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)
    # if request.method == "POST":
    #     serializer = ProgramSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def program_list(request):
    """
    API view function for List  out all program.
    """
    try:
        programs = Program.objects.all()
    except Program.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def program_detail_api(request, pk):
    """
    API function view for program details
    """
    program = Program.objects.get(id=pk)
    serializer = ProgramSerializer(program, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_program_api(request, pk):
    try:
        program = Program.objects.get(id=pk)
    except Program.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "DELETE":
        operation = program.delete()
        data = {}
        if operation:
            data["Delete"] = "Successful"

        else:
            data["Delete"] = "Failed"
        return Response(data=data)


@api_view(['POST'])
def program_update_api(request, pk):
    """
    API view function for add program....
    """
    program = Program.objects.get(id=pk)
    serializer = ProgramSerializer(instance=program, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
.......members API....... 
"""


@api_view(['GET', 'POST'])
def member_add_api(request):
    """
    API view function for add program....
    """
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def member_list_api(request):
    """
    api view for the member list...
    """
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def member_detail_api(request, pk):
    """
    API function view for program details
    """
    members = Member.objects.get(id=pk)
    serializer = MemberSerializer(members, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def member_update_api(request, pk):
    """
    API view function for add program....
    """
    members = Member.objects.get(id=pk)
    serializer = ProgramSerializer(instance=members, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
.......Supervisor API....... 
"""


@api_view(['GET', 'POST'])
def supervisor_add_api(request):
    """
    API view function for add supervisor....
    """
    serializer = SupervisorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def supervisor_list_api(request):
    """
    api view for the supervisor list...
    """
    supervisor = Supervisor.objects.all()
    serializer = SupervisorSerializer(supervisor, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def supervisor_detail_api(request, pk):
    """
    API function view for supervisor details
    """
    supervisor = Supervisor.objects.get(id=pk)
    serializer = SupervisorSerializer(supervisor, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def supervisor_update_api(request, pk):
    """
    API view function for update supervisor...
    """
    supervisor = Supervisor.objects.get(id=pk)
    serializer = SupervisorSerializer(instance=supervisor, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
.......Task API....... 
"""


@api_view(['GET', 'POST'])
def task_add_api(request):
    """
    API view function for add task....
    """
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def task_list_api(request):
    """
    api view for the task list...
    """
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail_api(request, pk):
    """
    API function view for task details
    """
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def task_update_api(request, pk):
    """
    API view function for update task...
    """
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
.......Project API....... 
"""


@api_view(['GET', 'POST'])
def project_add_api(request):
    """
    API view function for add project....
    """
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def project_list_api(request):
    """
    api view for the project list...
    """
    project = Project.objects.all()
    serializer = ProjectSerializer(project, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def project_detail_api(request, pk):
    """
    API function view for project details
    """
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def project_update_api(request, pk):
    """
    API view function for update project...
    """
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
