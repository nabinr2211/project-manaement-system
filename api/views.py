from django.shortcuts import render
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
    return Response(serializer.data)


@api_view(['GET'])
def program_list(request):
    """
    API view function for List all program.
    """
    programs = Program.objects.all()
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


@api_view(['GET','POST'])
def member_update_api(request, pk):
    """
    API view function for add program....
    """
    members = Member.objects.get(id=pk)
    serializer = ProgramSerializer(instance=members, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
