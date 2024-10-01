from django.urls import path
from .views import TeacherListView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView

urlpatterns = [
    path('',TeacherListView.as_view(),name="teachers_list"),
    path('create/',TeacherCreateView.as_view(),name="teacher_create"),
    # path('/update/<int:pk>',TeacherUpdateView.as_view(),name="teacher_update"),
    # path('/delete/<int:pk>',TeacherDeleteView.as_view(),name="teacher_delete")
]