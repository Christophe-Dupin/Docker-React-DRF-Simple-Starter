from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from app.posts.models import Post
from app.posts.api.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
