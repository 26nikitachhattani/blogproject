from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from blogs.models import blog
from .serializers import TaskSerializer
from rest_framework import status


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

@api_view(['POST'])
def BlogCreate(request):
    serializer = TaskSerializer(data=request.POST, files=request.FILES)
    
    if serializer.is_valid():
        obj=serializer.save(commit = False)
        obj.user = request.user
        obj.save()

    return Response(serializer.data)

@api_view(['POST'])
class FileUploadView(APIView):
    parser_class = (FileUploadParser)

    def post(self, request, *args, **kwargs):

      file_serializer = TaskSerializer(data=request.POST, files=request.FILES)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
