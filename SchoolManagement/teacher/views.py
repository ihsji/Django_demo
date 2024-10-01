from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.db.models import Q

from teacher.models import Teacher
from grades.models import Grade

class BaseTeacherView():
    model = Teacher
    success_url = reverse_lazy('teachers_list')#创建成功后重定向的URL

class TeacherListView(BaseTeacherView,ListView):
    template_name = 'teachers/teachers_list.html'
    context_object_name = 'teachers'
    pageinate = 10 #每页显示10行数据

    def get_queryset(self):
        queryset = super().get_queryset()
        grade_id = self.request.GET.get('grade') #获取班级 
        keyword = self.request.GET.get('search') #获取搜索内容
        if grade_id:
            queryset = queryset.filter(grade__pk = grade_id)
        if keyword:
            queryset = queryset.filter(
                Q(phone_number__startswith = keyword)|
                Q(phone_number__endswith = keyword)|
                Q(teacher_name__startswith = keyword)|
                Q(teacher_name__endswith = keyword)
            )
        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        # 获取所有班级并添加到上下文
        context['grade'] = Grade.objects.all().order_by('grade_number')
        context['current_grade'] = self.request.GET.get('grade','')
        return context



class TeacherCreateView(CreateView):
    pass

class TeacherUpdateView(UpdateView):
    pass

class TeacherDeleteView(DeleteView):
    pass