from rest_framework import serializers
from projects.models import Program, Member, Supervisor, Task, Project


class ProgramSerializer(serializers.ModelSerializer):
    """
    serializer class for the program
    """

    class Meta:
        model = Program
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    """
    serializer class for the member
    """
    class Meta:
        model = Member
        fields = '__all__'


class SupervisorSerializer(serializers.ModelSerializer):
    """
    serializer class for the supervisor
    """
    class Meta:
        model = Supervisor
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """
    serializer class for the supervisor
    """
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """
    serializer class for the supervisor
    """
    class Meta:
        model = Project
        fields = '__all__'
