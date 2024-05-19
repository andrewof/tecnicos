from rest_framework.routers import SimpleRouter

from users.api.api import UsersViewSet


router = SimpleRouter()

router.register('', UsersViewSet, basename='users')

urlpatterns = router.urls