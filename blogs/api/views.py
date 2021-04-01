from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogs.models import blog
from .serializers import TaskSerializer

# class blogListApiView(ListAPIView):
#     queryset = blog.objects.all()
#     serializer_class = TaskSerializer

@api_view(['GET'])
def blogListApiView(request):
    tasks=blog.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blogDetailApiView(request,pk):
    tasks=blog.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)
