from rest_framework import viewsets

from posts.models import Post
from posts.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("user")
    serializer_class = PostSerializer
