from django.db import models
from grades.models import Grade

# Create your models here.
class Teacher(models.Model):
    # user = models.OneToOneField(Grade,on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=50,name='老师姓名')
    phone_number = models.CharField(max_length=11,unique=True,name='手机号码')
    gender = models.CharField(max_length=1,name='性别')
    birthday = models.DateField(name="出生日期")
    # grade = models.OneToOneField(Grade,name="班级管理")