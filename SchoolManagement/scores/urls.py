from django.urls import path
from .views import ScoreListView,ScoreCreateView,ScoreUpdateView,ScoreDeleteView,ScoreDetailView

urlpatterns =[
    path('',ScoreListView.as_view(),name='score_list'),
    path('create/',ScoreCreateView.as_view(),name='score_create'),
    path('/detail/<int:pk>',ScoreDetailView.as_view(),name='score_detail'),
    path('/update/<int:pk>',ScoreUpdateView.as_view(),name='score_update'),
    path('delete/<int:pk>',ScoreDeleteView.as_view(),name='score_delete'),

]