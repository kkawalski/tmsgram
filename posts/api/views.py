from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from posts.models import Post
from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("user")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = self.queryset
        if not self.request.user.is_superuser:
            queryset = queryset.filter_is_active()
        return queryset

    def update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        post.is_active = False
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)