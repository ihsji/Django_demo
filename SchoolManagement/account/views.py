from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .forms import LoginForm
from students.models import Student
from teacher.models import Teacher

# Create your views here.
def user_login(request):
    #判断是否是post请求
    if request.method =='POST':
        #form表单验证
        form = LoginForm(request.POST)
        #验证失败
        if not form.is_valid():
            return JsonResponse({'status':'error','messages':'提交信息有误！'},status=400,safe=False)
        #验证成功
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        role =form.cleaned_data.get('role')
        #判断角色
        if role == 'teacher':
            try:
                teacher = Teacher.object.get(phone_number=username)
                username = teacher.teacher_name+'_'+teacher.phone_number
                user = authenticate(username=username,password=password)
            except Teacher.DoesNotExist:
                return JsonResponse({'status':'error','message':'老师信息不存在'},status=404)
        elif role =="student":
            try:
                student = Student.objects.get(username=username)
                username = student.student_name+"_"+student.student_number
                user = authenticate(username=username,password=password)
            except:
                return JsonResponse({'status':'error','messages':'学生信息不存在'}, status=404)
        
        else:
            try:
                user=authenticate(username=username,pasword=password)
            except:
                return JsonResponse({'status':'error', 'messages': '管理员信息不存在'}, status=404)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['username'] = username.split('_')[0]
                request.session['user_role'] = role
                return JsonResponse({'status':'success','messages':'登录成功'})
            else:
                return JsonResponse({'status':'error','messages':'账户已被禁用'},status=403)
        else:
            return JsonResponse({'staatus':'error','messages':'用户名或密码错误'},status=401)
        
    return render(request, 'accounts/login.html')

def user_logout(request):
    """退出登录"""
        # if 'user_role' in request.session:
    #     del request.session['user_role']
    logout(request)#执行退出
    #删除所有会话
    request.session.flush()
    return redirect('user_login')

def error_404_view(request,exception):
    return render(request,'404.html',{},status=404)