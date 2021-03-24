from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="myimages",blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    bio = models.TextField(default='no bio')
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    #def profile_post(self):
        #return self.blog_set.all()
    
    def __str__(self):
        return str(self.user.username)

    class meta:
        ordering = ('-created')
