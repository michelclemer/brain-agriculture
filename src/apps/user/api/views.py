from rest_framework.viewsets import ModelViewSet

from src.apps.user.api.serializers import UserSerializer
from src.apps.user.models import UserModel


class UserViewSet(ModelViewSet):
    permission_classes = []
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
