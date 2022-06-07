from django.urls import path

from posts.views import PostCreateView, PostDetailView


urlpatterns = [
    path("", PostCreateView.as_view(), name="post_list"),
    path("<int:pk>", PostDetailView.as_view(), name="post_detail"),
]
