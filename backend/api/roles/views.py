from rest_framework.viewsets import ModelViewSet

from backend.api.roles.models import Role
from backend.api.roles.serializers import RoleSerializer


class CommentViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
