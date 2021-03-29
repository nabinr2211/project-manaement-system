from django.db import models
from phone_field import PhoneField


# Create your models here.


class Program(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Supervisor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Member(models.Model):
    semester = (
        ('1st Sem', '1st sem'),
        ('2nd Sem', '2nd sem'),
        ('3rd Sem', '3rd sem'),
        ('4th Sem', '4th sem'),
        ('5th Sem', '5th sem'),
        ('6th Sem', '6th sem'),
        ('7th Sem', '7th sem'),
        ('8th Sem', '8th sem'),
    )
    symbol_no = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = PhoneField()
    semester = models.CharField(max_length=100, choices=semester)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project img')
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=False)
    task = models.ManyToManyField(Task)
    member = models.ManyToManyField(Member)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
