from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.conf import settings
import os
from django.http import Http404
from django.contrib.auth.hashers import make_password, check_password
from .serializer import (
    UserSerializer,
    ArticleSerializer,
    CommentSerializer,
    UserHeaderSerializer
)
from .models import (
    User,
    Article,
    Comment
)


class UserList(APIView):
    def get(self, request):   # get all the users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


"""
deal with the avatar of the user
"""


class Avatar(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'No such user'}, status=status.HTTP_404_NOT_FOUND)

        avatarserializer = UserHeaderSerializer(user)
        serializer_data = avatarserializer.data
        serializer_data['avatar'] = request.build_absolute_uri(
            serializer_data.get('avatar'))
        return Response({'success': 'Get success', 'data': serializer_data}, status=status.HTTP_200_OK)

    def put(self, request):
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'No such user'}, status=status.HTTP_404_NOT_FOUND)

        avatar = user.avatar
        if avatar:
            try:
                avatar.delete()  # Using Django's FileField delete method
            except Exception as e:
                return Response({'error': 'Delete avatar error'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserHeaderSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Put success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Userlogin(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')
        if account is None or password is None:
            return Response({'error': 'Please provide both account and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(account=account)
        if user is None:
            return Response({'error': 'No such user'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            hash_password = user.password  # get the hash password of the user
            # check if the password is correct
            boolean = check_password(password, hash_password)
            if boolean:
                return Response({'success': 'Login success', 'data': UserSerializer(user).data},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Wrong password'},
                                status=status.HTTP_400_BAD_REQUEST)


class Userregister(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        account = request.data.get('account')
        user = User.objects.filter(account=account)
        if user:
            return Response({'error': 'Account already exists'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            password = request.data.get('password')
            hash_password = make_password(password)  # hash the password
            password2 = request.data.get('password2')
            hash_password2 = make_password(password2)
            request.data['password'] = hash_password
            request.data['password2'] = hash_password2
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Register success', 'data': serializer.data},
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


# return all the articles

class AllArticl(APIView):
    def get(self, request):
        articles = Article.objects.all()
        for article in articles:
            comments = Comment.objects.filter(article=article)
            serializer_comment = CommentSerializer(comments, many=True)
            comments_count = len(serializer_comment.data)
            article.comments_count = comments_count
            article.save()
        for article in articles:
            likes = article.get_likes_count()  # get the number of likes of the article
            article.likes_count = likes
            article.save()
        serializer_article = ArticleSerializer(articles, many=True)
        return Response({'success': 'Get success', 'data': serializer_article.data}, status=status.HTTP_200_OK)


# return the user_id of the user's articles
class ArticleList(APIView):
    def get(self, request, user_id):
        user = User.objects.get(user_id=user_id)
        articles = user.article_set.all()
        for article in articles:
            comments = Comment.objects.filter(article=article)
            serializer_comment = CommentSerializer(comments, many=True)
            comments_count = len(serializer_comment.data)
            article.comments_count = comments_count
            article.save()
        for article in articles:
            likes = article.get_likes_count()
            article.likes_count = likes
            article.save()
        serializer_article = ArticleSerializer(articles, many=True)
        return Response(serializer_article.data)


class ArticleDetail(APIView):
    def get(self, request):
        article_id = request.data.get('article_id')
        # use the article_id to get the article
        article = Article.objects.get(id=article_id)
        likes = article.get_likes_count()
        comments = CommentSerializer(
            Comment.objects.filter(article=article), many=True)
        if article:
            return Response({'success': 'Get success', 'data': ArticleSerializer(article).data, 'likes': likes, 'comments': len(comments.data)},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No such article'},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            user = User.objects.get(user_id=request.data.get('author'))
            content = request.data.get('content')
            # use the user_id and content to create an article
            articleserializer = ArticleSerializer(
                data={'author': user.user_id, 'content': content})
            if articleserializer.is_valid():
                article = articleserializer.save()
                return Response({'success': 'Post success', 'data': ArticleSerializer(article).data},
                                status=status.HTTP_201_CREATED)
            else:
                return Response(articleserializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'No such user'},
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        article_id = request.data.get('article_id')
        article = Article.objects.get(id=article_id)
        articel_serializer = ArticleSerializer(article, data=request.data)
        if articel_serializer.is_valid():
            articel_serializer.save()
            return Response({'success': 'Put success', 'data': articel_serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response(articel_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        article_id = request.data.get('article_id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            return Response({'success': 'Delete success'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No such article'},
                            status=status.HTTP_400_BAD_REQUEST)


class CommentList(APIView):
    def get(self, request, user_id, article_id):
        user = User.objects.get(user_id=user_id)
        article = Article.objects.get(id=article_id, author=user)
        # use the article_id to get the comments of the article
        comment = Comment.objects.filter(article=article)
        comment_serializer = CommentSerializer(comment, many=True)
        if comment_serializer:
            return Response({'success': 'Get success', 'data': comment_serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No such comment'},
                            status=status.HTTP_400_BAD_REQUEST)


class Commentdetail(APIView):
    def post(self, request):
        try:
            user_id = request.data.get('user_id')
            user = User.objects.get(user_id=user_id)
            article_id = request.data.get('article_id')
            article = Article.objects.get(id=article_id)
            comment_serializer = CommentSerializer(
                data={'author': user.user_id, 'article': article.id, 'comment': request.data.get('comment')})
            if comment_serializer.is_valid():
                comment = comment_serializer.save()
                return Response({'success': 'Post success', 'data': CommentSerializer(comment).data},
                                status=status.HTTP_201_CREATED)

            else:
                return Response(comment_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'error': 'No such user or article'},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        comment_id = request.data.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        if comment:
            comment.delete()
            return Response({'success': 'Delete success'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No such comment'},
                            status=status.HTTP_400_BAD_REQUEST)


class Likes(APIView):

    def post(self, request):
        article_id = request.data.get('article_id')
        article = Article.objects.get(id=article_id)
        user_id = request.data.get('user_id')
        user = User.objects.get(user_id=user_id)
        try:
            if article.likes.filter(user_id=user_id).exists():
                # if the user has liked the article, then unlike it
                article.likes.remove(user)
                return Response({'success': 'Unlike success'},
                                status=status.HTTP_200_OK)
            else:
                article.likes.add(user)
                return Response({'success': 'Like success'},
                                status=status.HTTP_200_OK)
        except:
            return Response({'error': 'No such user or article'},
                            status=status.HTTP_400_BAD_REQUEST)
