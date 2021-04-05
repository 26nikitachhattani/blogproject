from rest_framework.serializers import ModelSerializer, FileField
from rest_framework import serializers
from django.contrib.auth.models import User
from blogs.models import blog


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class TaskSerializer(ModelSerializer):
    class Meta:
        
        model = blog
        photo = FileField()
        fields = ['name' , 'photo' , 'desc']
        #fields = '__all__'