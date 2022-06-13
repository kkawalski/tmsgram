from os import stat
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from core.api.serializers import UserBaseSerializer, UserSerializer, FollowerSerializer
from core.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related("posts")
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ["created_at", "id"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserBaseSerializer
        if self.action == "followers":
            return FollowerSerializer
        return self.serializer_class
    
    @action(methods=["GET"], detail=True)
    def followers(self, request, pk=None):
        user = self.get_object()
        followers = user.followers
        res_data = self.get_serializer(instance=followers, many=True).data
        return Response(res_data, status=status.HTTP_200_OK)
