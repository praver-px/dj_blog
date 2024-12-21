from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=100)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_DEFAULT, default=1)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class BlogComment(models.Model):
    content = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
