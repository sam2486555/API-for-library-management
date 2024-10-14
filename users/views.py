from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'retrieve', 'update'):
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class UserUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()

    def get_permissions(self):
        if self.action in ('destroy', 'retrieve', 'update'):
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'retrieve', 'update'):
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ('destroy', 'retrieve', 'update'):
            self.permission_classes = (IsOwner,)
        return super().get_permissions()
