from shutil import register_unpack_format
from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from rest_framework.decorators import api_view

from project.api.models import Post
from project.api.serializers import PostCreateSerializer, PostSelectSerializer, PostUpdateSerializer

# Create your views here.

#@api_view(['GET'])
class PostCreateSelect(APIView):
    def post(self, request):
        serializer = PostCreateSerializer(data = request.data)        
        serializer.is_valid(raise_exception=True)

        instance = PostSelectSerializer(serializer.save()).data

        return Response(instance, status=status.HTTP_201_CREATED)

    def get(self, _):
        queryset = Post.objects.all()

        # print(f"Title: {queryset[0].id}")
        serializer = PostSelectSerializer(queryset, many = True)
        
        return Response(serializer.data)

class PostDeleteUpdate(APIView):
    def delete(self, request, id: int):
        instance = Post.objects.filter(id = id)
        
        print(instance, len(instance))
        if len(instance) == 0:
            return Response("No Content", status=status.HTTP_204_NO_CONTENT)
        instance.delete()
        return Response("Ok", status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id : int):
        serializer = PostUpdateSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        instance = Post.objects.filter(id = id)
        
        if len(instance) == 0:
            return Response("No Content", status=status.HTTP_204_NO_CONTENT)
 
        instance = serializer.update(instance[0], serializer.data)
        
        instance = PostSelectSerializer(instance).data

        return Response(instance)
