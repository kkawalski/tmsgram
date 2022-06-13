from rest_framework import serializers

from core.models import User


class FollowerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]

class UserBaseSerializer(serializers.ModelSerializer):
    followers_cnt = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "followers_cnt",
            "full_name",
        ]

    def get_followers_cnt(self, obj):
        return obj.followers.count()


from posts.api.serializers import PostBaseSerializer

class UserSerializer(serializers.ModelSerializer):
    posts = PostBaseSerializer(many=True)

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
