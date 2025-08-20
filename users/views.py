from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.permissions import IsStaff
from users.serializers import UserSerializer, UserSerializerNoPass


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializerNoPass
    queryset = User.objects.all()
    permission_classes = [IsStaff]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializerNoPass
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsStaff]
