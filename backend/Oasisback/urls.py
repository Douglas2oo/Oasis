from . import views
from django.shortcuts import render
from django.views.static import serve
from django.conf import settings
from django.urls import path,re_path




def home_view(request):
    return render(request, 'home.html')




urlpatterns = [
    path("login/", views.Userlogin.as_view(), name="login"),
    path("register/", views.Userregister.as_view(),name="register"),
    path('', home_view, name='home'),
    path('articlelist/user_id/<str:user_id>', views.ArticleList.as_view(), name='article_list'),
    path('article/', views.ArticleDetail.as_view(), name='article_detail'),
    path('articlelist/', views.AllArticl.as_view(), name='all_article'),
    path('commentlist/user_id/<str:user_id>/article_id/<int:article_id>', views.CommentList.as_view(), name='comment_list'),
    path('comment/', views.Commentdetail.as_view(), name='comment'),
    path('likes/', views.Likes.as_view(), name='likes'),
    path('avatar/', views.Avatar.as_view(), name='avatar'),
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT
    }) # serve the media files
]