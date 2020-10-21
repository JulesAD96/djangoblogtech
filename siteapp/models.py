from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(verbose_name="Post title", max_length=255)
    slug = models.SlugField(verbose_name="Post slug")
    image = models.ImageField(upload_to="upload/siteapp/%Y")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_commented = models.ForeignKey(Post,verbose_name="Post commented", 
                                       on_delete=models.CASCADE)
    body_comment = models.TextField(verbose_name="Your comment")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.author)
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
    