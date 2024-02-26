from rest_framework import routers

from .views import AgriculteViewSet, PlantedCropsViewSet

router = routers.DefaultRouter()
router.register(r'proprietarios', AgriculteViewSet)
router.register(r'culturas-plantadas', PlantedCropsViewSet)
urlpatterns = router.urls
