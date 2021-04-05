from rest_framework.serializers import ModelSerializer, FileField
from django.contrib.auth.models import User
from blogs.models import blog

class TaskSerializer(ModelSerializer):
    class Meta:
        
        model = blog
        photo = FileField()
        fields = ['name' , 'photo' , 'desc']
        #fields = '__all__'