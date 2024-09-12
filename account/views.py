from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.POST:
        username=request.POST.get("username")
        password=request.POST.get("password")
        return HttpResponse(f"使用POST方式提交用户名：{username} 密码：{password}")
    elif request.methon=="GET":
        return render(request,"login.html")
