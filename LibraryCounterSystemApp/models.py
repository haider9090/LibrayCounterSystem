from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=50, default=False)
    lastname = models.CharField(max_length=50, default=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=50, null=False)
    image = models.ImageField(default='default.png', blank=True)
    isActive = models.BooleanField(default=True)


# Create your models here.
class Unknown(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(default='default.png', blank=True)
    entry = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(auto_now_add=True)


# Create your models here.
class StudentBatch(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    bid = models.ForeignKey(StudentBatch, on_delete=models.CASCADE)


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)


# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=50, null=False)


# Create your models here.
class Semester(models.Model):
    sno = models.IntegerField(null=False)


# Create your models here.
class StudentSemester(models.Model):
    std = models.ForeignKey(Student, on_delete=models.CASCADE)
    smd = models.ForeignKey(Semester, on_delete=models.CASCADE)


# Create your models here.
class Visitor(models.Model):
    std = models.ForeignKey(Student, on_delete=models.CASCADE)
    enter = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(auto_now_add=True)
