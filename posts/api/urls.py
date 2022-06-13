from django.urls import URLPattern
from rest_framework import routers

from posts.api.views import PostViewSet


router = routers.DefaultRouter()
router.register("api", PostViewSet)
urlpatterns = router.urls
