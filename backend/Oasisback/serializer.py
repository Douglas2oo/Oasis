from rest_framework import serializers
from .models import User, Article, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'create_time', 'name', 'email', 'account', 'birthday', 'password', 'password_2']



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['author', 'content', 'create_time', 'likes']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'article', 'content', 'create_time']


