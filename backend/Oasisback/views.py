from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializer import (
    UserSerializer,
    ArticleSerializer,
    CommentSerializer,
)
from .models import (
    User, 
    Article, 
    Comment
    )


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



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
            if user.password == password:
                return Response({'success': 'Login success'},
                            status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Wrong password'},
                            status=status.HTTP_400_BAD_REQUEST)
            

class Userregister(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)



    def post(self,request):
        account = request.data.get('account')
        user = User.objects.filter(account=account)
        if user:
            return Response({'error': 'Account already exists'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': 'Register success', 'data':serializer.data},
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    

class ArticleList(APIView):
    def get(self, request,user_id):
        user = User.objects.get(user_id=user_id)
        serializer_article = ArticleSerializer(user.article_set.all(), many=True)
        return Response(serializer_article.data)
    


class ArticleDetail(APIView):
    def get(self, request):
            article_id = request.data.get('article_id')
            article = Article.objects.get(id=article_id)
            if article:
                return Response({'success': 'Get success', 'data':ArticleSerializer(article).data},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'No such article'},
                                status=status.HTTP_400_BAD_REQUEST)
                



    def post(self,request):
        try:
            user = User.objects.get(user_id=request.data.get('author'))
            content = request.data.get('content')
            articleserializer = ArticleSerializer(data={'author':user.user_id, 'content':content})
            if articleserializer.is_valid():
                article = articleserializer.save()
                return Response({'success': 'Post success', 'data':ArticleSerializer(article).data},
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
                    return Response({'success': 'Put success', 'data':articel_serializer.data},
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
    def get(self, request,user_id,article_id):
        user = User.objects.get(user_id=user_id)
        article = Article.objects.get(id=article_id, author=user)
        comment = Comment.objects.filter(article=article)
        comment_serializer = CommentSerializer(comment, many=True)
        if comment_serializer:
            return Response({'success': 'Get success', 'data':comment_serializer.data},
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
            comment_serializer = CommentSerializer(data={'author':user.user_id, 'article':article.id, 'comment':request.data.get('comment')})
            if comment_serializer.is_valid():
                comment = comment_serializer.save()
                return Response({'success': 'Post success', 'data':CommentSerializer(comment).data},
                                status=status.HTTP_201_CREATED)
            
            else:
                return Response(comment_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
            

        except:
            return Response({'error': 'No such user or article'},
                            status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request):
        comment_id = request.data.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
        if comment:
            comment.delete()
            return Response({'success': 'Delete success'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No such comment'},
                            status=status.HTTP_400_BAD_REQUEST)