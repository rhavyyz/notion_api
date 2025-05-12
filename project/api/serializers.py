from rest_framework import serializers

from project.api.models import Post


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
        fields=['id','username', 'title', 'content', 'created_datetime']

    def save(self):
        raise Exception("This post serializer is only ment to reading operations") 
    def update(self, instance, validated_data):
        raise Exception("This post serializer is only ment to reading operations")
    def create(self,validated_data):
        raise Exception("This post serializer is only ment to reading operations")

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=['title', 'content']

    def create(self,validated_data):
        raise Exception("This post serializer is only ment to update posts")
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
        raise Exception("This post serializer is only ment to create posts")
    def create(self,validated_data):
        return Post.objects.create(**validated_data)
    
