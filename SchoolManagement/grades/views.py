from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from grades.models import Grade
from django.db.models import Q
from grades.forms import GradeForm
from django.urls import reverse_lazy

# Create your views here.
class GradeListView(ListView):
    model = Grade #引入Grade模型
    template_name = 'grades/grades_list.html' #引入模板文件
    fields = ['grade_name','grade_number']    #模板的字段
    context_object_name = 'grades'
    paginate_by = 10
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset =  super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(grade_name__icontains=search)|
                Q(grade_number__icontains=search)
            )
        return queryset
    

class GradeUpdateView(UpdateView):
    model = Grade
    template_name = 'grades/grades_form.html' 
    form_class = GradeForm
    success_url = reverse_lazy('grades_list')



class GradeCreateView(CreateView):
    model = Grade
    template_name = 'grades/grades_form.html' 
    form_class = GradeForm
    success_url = reverse_lazy('grades_list')

class GradeDeleteView(DeleteView):
    model = Grade
    template_name = 'grades/grade_delete_confirm.html'
    success_url = reverse_lazy('grades_list')