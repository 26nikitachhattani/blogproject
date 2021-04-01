from rest_framework.serializers import ModelSerializer
from blogs.models import blog

class TaskSerializer(ModelSerializer):
    class Meta:
        model = blog
        fields = '__all__'