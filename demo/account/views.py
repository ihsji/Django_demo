from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        return HttpResponse(f"使用POST方式提交用户名：{username} 密码：{password}")
    if request.method=="GET":
        return render(request,"laccount_login.html")

class RegisterView(View):
    def get(self,request):
        return render(request, "account_register.html")
    
    def post(self,request):
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        return HttpResponse(f"使用POST方式提交用户名：{username} 密码：{password}")
