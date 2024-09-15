from django.contrib import admin
from slide.models import Slide

# Register your models here.

class SlideAdmin(admin.ModelAdmin):
    #列表显示
    list_display = ['id','title']
    #搜索框
    search_fields = ['title','id']

admin.site.register(Slide,SlideAdmin)

