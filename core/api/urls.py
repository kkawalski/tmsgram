from rest_framework import routers

from core.api.views import UserViewSet


router = routers.DefaultRouter()
router.register("api", UserViewSet)
urlpatterns = router.urls
