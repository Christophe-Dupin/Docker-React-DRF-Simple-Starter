from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.posts.api.views import PostViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.register("post", PostViewSet)


app_name = "api"
urlpatterns = router.urls
