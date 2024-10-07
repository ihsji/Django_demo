# 导入 REST Framework 中的序列化模块和 movie 应用中的电影模型
from rest_framework import serializers
from movie.models import Movie,Category

# 定义电影序列化器类
class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        # 指定序列化器所使用的模型
        model = Movie
        # 指定需要序列化的字段为所有字段
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
