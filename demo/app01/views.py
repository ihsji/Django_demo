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

def list(request):
    author="andy"
    article_number = 20
    article_list = [
        '第一篇文章: 什么是django',
        '第二篇文章: django的mvt模式',
        '第三片文章: django的视图'
    ]
    info = {
        'name': 'andy',
        'age': 30,
        'programming_language': ['python','java','c']
    }
    return render(request,"app01_list.html",{
        "author":author,
        "article_number":article_number,
        'article_list': article_list,
        'info': info
    })