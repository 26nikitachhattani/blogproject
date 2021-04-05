from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from blogs.models import blog
from .serializers import TaskSerializer, RegisterSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework import status
from knox.models import AuthToken


# class blogListApiView(ListAPIView):
#     queryset = blog.objects.all()
#     serializer_class = TaskSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class awsimageView(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user = request.user)
        return Response(serializer.data)



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

# @api_view(['POST'])
# def BlogCreate(request):
#     serializer = TaskSerializer(data=request.POST, files=request.FILES)
    
#     if serializer.is_valid():
#         obj=serializer.save(commit = False)
#         obj.user = request.user
#         obj.save()

#     return Response(serializer.data)

# @api_view(['POST'])
# class FileUploadView(APIView):
#     parser_class = (FileUploadParser)

#     def post(self, request, *args, **kwargs):

#       file_serializer = TaskSerializer(data=request.POST, files=request.FILES)

#       if file_serializer.is_valid():
#           file_serializer.save()
#           return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#       else:
#           return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
