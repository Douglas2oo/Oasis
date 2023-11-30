from rest_framework import serializers
from .models import User, Article, Comment


"""
Serializer is used to serialize and deserialize data for individual models,
and is used to convert the data into a format that can be easily rendered to JSON
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'create_time', 'name', 'email', 'account', 'birthday', 'password', 'password2']

class UserHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id","avatar"]



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','author', 'content', 'create_time', 'likes', 'likes_count','comments_count']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','author', 'article', 'comment', 'create_time']