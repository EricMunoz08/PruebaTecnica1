from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projectos', ProjectViewSet, 'projectos')
urlpatterns = router.urls