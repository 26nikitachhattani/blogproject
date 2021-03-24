from django.db import models
from django.conf import settings
from django.contrib.auth.models import User , auth
from profiles.models import Profile
from django.utils.timezone import now


# Create your models here.

user = settings.AUTH_USER_MODEL 

class blog(models.Model):
    user = models.ForeignKey(User,
                        default = 1, 
                        null = True,  
                        on_delete = models.SET_NULL 
                        ) 
    name = models.CharField(max_length=200,default=None)
    photo = models.ImageField(upload_to="myimages")
    desc = models.TextField(default="post")
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def number_of_likes(self):
        return self.likes.count()

    

class CommentModel(models.Model):
    your_name = models.CharField(max_length=20)
    comment_text = models.TextField()
    blog = models.ForeignKey('blog', on_delete=models.CASCADE)
    date = models.DateTimeField(default=now, blank=True)
     
    def __str__(self):
        return f"Comment by Name: {self.your_name}"