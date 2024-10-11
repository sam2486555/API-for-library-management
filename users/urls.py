from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (UserCreateAPIView, UserDestroyAPIView,
                         UserListAPIView, UserRetrieveAPIView,
                         UserUpdateAPIView)

app_name = UsersConfig.name
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('create/', UserCreateAPIView.as_view(permission_classes=(AllowAny,)), name='create'),
    path('retrieve/<int:pk>/', UserRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('destroy/<int:pk>/', UserDestroyAPIView.as_view(), name='destroy'),
    path('list/', UserListAPIView.as_view(), name='list')
]
