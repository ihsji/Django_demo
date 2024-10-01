from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.db.models import Q

from .models import Score
from .forms import ScoreForm
from grades.models import Grade

# Create your views here.
class BaseScoreView():
    model = Score
    success_url = reverse_lazy('score_list') # 创建成功后重定向的URL
    # allowed_role=['admin','teacher'] # 设置允许访问的角色



class ScoreListView(BaseScoreView,ListView):
    template_name = 'scores/score_list.html'
    context_object_name = 'scores'
    paginate = 10

    def get_context_data(self,**kwargs):
        context = super(ScoreListView,self).get_context_data(**kwargs)
        context['grades'] = Grade.objects.all()
        context['current_grade'] = self.request.GET.get('grade','')
        return context



class ScoreListView(BaseScoreView, ListView):
    template_name = 'scores/score_list.html'
    context_object_name = 'scores'
    paginate_by = 10  # 每页显示10条数据

    def get_queryset(self):
        queryset = super().get_queryset()
        grade_query = self.request.GET.get('grade')  # 从GET请求中获取班级查询参数
        search_query = self.request.GET.get('search')  # 获取搜索查询参数

        if grade_query:
            queryset = queryset.filter(grade__pk=grade_query)
        if search_query:
            queryset = queryset.filter(
                Q(student_number__icontains=search_query) | 
                Q(student_name__icontains=search_query)
            )
        return queryset.order_by('grade', 'student_number')
    
    def get_context_data(self, **kwargs):
        context = super(ScoreListView, self).get_context_data(**kwargs)
        # 获取所有班级并添加到上下文
        context['grades'] = Grade.objects.all()
        context['current_grade'] = self.request.GET.get('grade', '')  # 获取当前查询的班级ID
        return context

# ScoreCreateView, ScoreUpdateView, ScoreDeleteView,ScoreDeleteMultipleView
class ScoreCreateView(BaseScoreView, CreateView):
    form_class = ScoreForm
    template_name = 'scores/score_form.html'  # 指定使用的模板文件

    
class ScoreUpdateView(BaseScoreView, UpdateView):
    form_class = ScoreForm
    template_name = 'scores/score_form.html'  # 指定使用的模板文件

class ScoreDeleteView(BaseScoreView, DeleteView):
    # template_name_suffix = "_form"  #在template_name相对路径下找到后缀为_form的html文件渲染上下文。

    def delete(self, request, *args,**kwargs):
    #这里检查是否是AJAX请求
        if request.headers.get("X_Requested-with") == 'XMLHttpRequest':
            response = super().delete(request, *args,**kwargs)
            if response.status_code == 302:
                return JsonResponse({'status': 'success', 'messages': '学生已删除'})
            else:
                return JsonResponse({'status': 'error', 'messages': '删除失败'}, status=400)
        else:
            return super().delete(request, *args, **kwargs)



class ScoreDetailView(BaseScoreView, DetailView):
    pass