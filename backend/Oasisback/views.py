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
        