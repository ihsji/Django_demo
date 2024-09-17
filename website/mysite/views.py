from django.http import HttpResponse
from django.shortcuts import render
from slide.models import Slide
from team.models import Team
from news.models import News

# Create your views here.
def index(request):
    # 获取slide表数据
    slides = Slide.objects.all()
    # 获取团队成员
    team = Team.objects.all().order_by('-rank')
    # 获取咨询中心新闻
    news = News.objects.filter(category_id=1).order_by('-created_at')[:3]
    # 获取成功案例内容
    cases = News.objects.filter().exclude(category_id=1).order_by('-created_at')[:6]
    print(cases)
    return render(request, 'index.html', {
                      'slides': slides,
                      'team': team,
                      'news': news,
                      'cases': cases,
                      })