from django.core import validators
from django import forms
from .models import blog

class ImageForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['name' , 'photo' , 'desc']
        labels = {'photo':''}

class CommentForm(forms.Form):
    #your_name =forms.CharField(max_length=20)
    comment_text =forms.CharField(widget=forms.TextInput)
 
    def __str__(self):
        return f"{self.comment_text} by {self.your_name}"