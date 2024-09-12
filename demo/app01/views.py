from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloworld(request):
    return HttpResponse("hello world")

def article_create(request):
    return HttpResponse("创建一篇文章")

def article_detail(request,article_id,title):
    return HttpResponse(f"文章的id是：{article_id},标题是:{title}")

def phone_detail(request,phone_number):
    return HttpResponse("用户手机号为：{phone_number}")