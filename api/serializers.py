from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']



class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # comments = serializers.SlugRelatedField(slug_field="body", many=True, read_only=True)
    comments = CommentSerializer(many=True)
    categories = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments', 'categories']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(slug_field="title", many=True, read_only=True)
    comments = serializers.SlugRelatedField(slug_field="body", many=True, read_only=True)
    categories = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'comments', 'categories']




