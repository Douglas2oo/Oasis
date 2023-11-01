from django.urls import path
from . import views
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')




urlpatterns = [
    path("login/", views.Userlogin.as_view(), name="login"),
    path("register/", views.Userregister.as_view(),name="register"),
    path('', home_view, name='home'),
    path('articlelist/user_id/<str:user_id>', views.ArticleList.as_view(), name='article_list'),
    path('article/', views.ArticleDetail.as_view(), name='article_detail'),
    # path('comment/', views.CommentList.as_view(), name='comment')
]