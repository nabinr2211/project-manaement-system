from rest_framework import serializers
from projects.models import Program, Member


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
