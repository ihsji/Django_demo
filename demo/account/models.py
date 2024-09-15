from django.db import models
from utils.basemodels import BaseModels
# Create your models here.
class User(BaseModels):
    id = models.AutoField(primary_key=True) #在数据库里创建一个id的字段，它使用一个主键约束、自增约束的列
    username = models.CharField("用户名",max_length=30,null=True,blank=True,unique=True)
    password = models.CharField("密码",max_length=30)
    email = models.EmailField("邮箱",null=True,blank=True,unique=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户信息'

    def __str__(self):
        return self.username