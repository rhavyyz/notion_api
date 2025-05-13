from shutil import register_unpack_format
from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from rest_framework.decorators import api_view

from project.api.models import Comment, Post, Like
from project.api.serializers import CommentPostCreateSerializer, CommentPostSelectSerializer, LikePostCreateSerializer, PostCreateSerializer, PostSelectSerializer, PostUpdateSerializer, CommentCommentSelectSerializer, CommentCommentCreateSerializer, LikeCommentCreateSerializer

# Create your views here.

"""

    LIKE VIEWS

"""

class LikePostCreateDelete(APIView):
    def post(self, request, id, username):
        serializer = LikePostCreateSerializer(data = {'post': id, 'username': username})
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response("Created", status=status.HTTP_201_CREATED)
    def delete(self, request, id, username):
        instance = Like.objects.filter(post__id=id, username=username)
        if len(instance) == 0:
            return Response("No Content", status=status.HTTP_204_NO_CONTENT)

        instance.delete()

        return Response("Ok")

class LikeCommentCreateDelete(APIView):
    def post(self, request, id, username):
        serializer = LikeCommentCreateSerializer(data = {'comment': id, 'username': username})
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response("Created", status=status.HTTP_201_CREATED)
    def delete(self, request, id, username):
        instance = Like.objects.filter(comment__id=id, username=username)
        if len(instance) == 0:
            return Response("No Content", status=status.HTTP_204_NO_CONTENT)

        instance.delete()

        return Response("Ok")




"""

    COMMENT VIEWS

"""

class CommentPostCreateSelect(APIView):
    def get(self, _, id):
        data = Comment.objects.filter(post__id=id)
        return Response(CommentPostSelectSerializer(data, many = True).data)

    def post(self, request, id):
        if 'post' in request.data:
            del request.data['post']
        serializer = CommentPostCreateSerializer(data = {**request.data, "post":id})
        serializer.is_valid(raise_exception = True)
        instance = CommentPostSelectSerializer(serializer.save()).data
        
        return Response(instance, status=status.HTTP_201_CREATED)

class CommentCommentCreateSelect(APIView):
    def get(self, _, id):
        data = Comment.objects.filter(comment__id=id)
        return Response(CommentCommentSelectSerializer(data, many = True).data)

    def post(self, request, id):
        if 'comment' in request.data:
            del request.data['comment']
        serializer = CommentCommentCreateSerializer(data = {**request.data, "comment":id})
        serializer.is_valid(raise_exception = True)
        instance = CommentCommentSelectSerializer(serializer.save()).data
        
        return Response(instance, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def comment_delete(_, id):
    instance = Comment.objects.filter(id=id)
    
    if len(instance) == 0:
        return Response("No Content", status=status.HTTP_204_NO_CONTENT)
    
    instance.delete()
    return Response("Ok")

"""

    POST VIEWS

"""

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
