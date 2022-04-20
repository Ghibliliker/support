from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.serializers import CustomUserCreateSerializer, CustomUserSerializer
from users.permissions import MePermission
from users.mixins import CreateListViewSet


class UserViewSet(CreateListViewSet):
    """Users view for create or get users"""
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CustomUserSerializer
        return CustomUserCreateSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(
        detail=False,
        methods=['get', 'patch'],
        permission_classes=[MePermission],
    )
    def me(self, request) -> Response:
        """for update or get information of current user"""
        user = self.request.user

        if request.method == 'GET':
            serializer = CustomUserSerializer(user)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        if request.method == 'PATCH':
            serializer = CustomUserCreateSerializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
