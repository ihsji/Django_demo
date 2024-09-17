from django.shortcuts import render
from django.views.generic import ListView
from .models import Grade

# Create your views here.
class GradeListView(ListView):
    model = Grade #引入Grade模型
    template_name = 'grades/grades_list.html'
    fields = ['grade_name','grade_number']
    context_object_name = 'grades'