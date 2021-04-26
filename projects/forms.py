from django import forms
from projects.models import *


class AddProgramModelsForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'






class EditProgramModelsForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'


class AddMemberModelsForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class EditMemberModelsForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class AddSupervisorModelsForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = '__all__'


class EditSupervisorModelsForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = '__all__'


class AddTaskModelsForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class EditTaskModelsForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class AddProjectModelsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        # widget=forms.TextInput(attrs={'class':"start_date",'placeholder':"mm/dd/yyyy"})


class EditProjectModelsForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

