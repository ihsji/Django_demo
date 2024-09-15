from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField('头像', upload_to='avator', help_text="最佳尺寸为800.*600" )
    name = models.CharField("姓名", max_length = 200, help_text="人物名称" )
    title = models.CharField("职务", max_length=200, help_text="人物职务" )
    rank = models.IntegerField("排序")



    class Meta:
        db_table = 'team'
        verbose_name = '团队管理'
        verbose_name_plural = '团队人物信息管理'

    def __str__(self):
        return self.name