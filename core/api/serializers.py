from rest_framework import serializers

from core.models import User
from posts.api.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "posts",
        ]
