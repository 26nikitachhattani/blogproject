from django.contrib import admin
from .models import blog, CommentModel

# Register your models here.
@admin.register(blog)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name','user','photo','desc','date')

@admin.register(CommentModel)
class commentadmin(admin.ModelAdmin):
    list_display = ('id' ,'your_name','comment_text','blog')



