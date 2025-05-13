from rest_framework import serializers

from project.api.models import Comment, Like, Post

"""

    LIKE SERIALIZERS

    -- username
    -- post
    -- comment

"""

class LikeCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['comment', 'username']
    def update(self, instance, validated_data):
        raise Exception("This like serializers is only meant to create operations")
    def create(self, validated_data):
        return Like.objects.create(**validated_data)

class LikePostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'username']
    def update(self, instance, validated_data):
        raise Exception("This like serializers is only meant to create operations")
    def create(self, validated_data):
        return Like.objects.create(**validated_data)

"""

    COMMENT SERIALIZERS

    -- username
    -- post  
    -- comment
    -- content
    -- created_datetime
    -- like_qtd

"""

class CommentPostSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_datetime', 'username', 'post', 'like_qtd']

    def save(self):
        raise Exception("This comment serializer is only meant to reading operations") 
    def update(self, instance, validated_data):
        raise Exception("This comment serializer is only meant to reading operations")
    def create(self,validated_data):
        raise Exception("This comment serializer is only meant to reading operations")



class CommentCommentSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_datetime', 'username', 'comment', 'like_qtd']
    def save(self):
        raise Exception("This comment serializer is only meant to reading operations") 
    def update(self, instance, validated_data):
        raise Exception("This comment serializer is only meant to reading operations")
    def create(self,validated_data):
        raise Exception("This comment serializer is only meant to reading operations")



class CommentPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields=['username', 'post', 'content']
    
    def update(self, instance, validated_data):
        raise Exception("This comment serializer is only meant to create comments")
    def create(self,validated_data):
        print(validated_data)
        return Comment.objects.create(**validated_data)
    
class CommentCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields=['username', 'comment', 'content']
    
    def update(self, instance, validated_data):
        raise Exception("This comment serializer is only meant to create comments")
    def create(self,validated_data):
        print(validated_data)
        return Comment.objects.create(**validated_data)
    

"""
    
    POST SERIALIZERS
    
    -- id
    -- username
    -- title
    -- content
    -- created_datetime

"""

class PostSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=['id','username', 'title', 'content', 'created_datetime', 'like_qtd']

    def save(self):
        raise Exception("This post serializer is only meant to reading operations") 
    def update(self, instance, validated_data):
        raise Exception("This post serializer is only meant to reading operations")
    def create(self,validated_data):
        raise Exception("This post serializer is only meant to reading operations")

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=['title', 'content']

    def create(self,validated_data):
        raise Exception("This post serializer is only meant to update posts")
    def update(self, instance : Post, validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.save()

        return instance

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=['username','title', 'content']

    def update(self, instance, validated_data):
        raise Exception("This post serializer is only meant to create posts")
    def create(self,validated_data):
        return Post.objects.create(**validated_data)
    
