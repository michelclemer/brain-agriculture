from rest_framework import routers

from .views import CityViewSet, CountryViewSet, StateViewSet

router = routers.DefaultRouter()
router.register(r'cidades', CityViewSet)
router.register(r'paises', CountryViewSet)
router.register(r'estados', StateViewSet)

urlpatterns = router.urls

