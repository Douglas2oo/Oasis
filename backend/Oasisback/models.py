from django.db import models
import uuid



# Create your models here.

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    account = models.CharField(max_length=50)
    birthday = models.DateField()
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)





class Article(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)


    def __str__(self):
        return self.content
    

    def get_likes_count(self):
        return self.likes.count()
    




class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='comments')
    comment = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content
    


owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
highlighted = models.TextField()