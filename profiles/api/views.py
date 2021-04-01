from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profiles.models import Profile
from .serializers import ProfileSerializer

# class blogListApiView(ListAPIView):
#     queryset = blog.objects.all()
#     serializer_class = TaskSerializer

@api_view(['GET'])
def profileListApiView(request):
    tasks=Profile.objects.all().order_by('-id')
    serializer = ProfileSerializer(tasks, many=True)
    return Response(serializer.data)


