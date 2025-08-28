from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'tg_chat_id')


class UserSerializerNoPass(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'tg_chat_id')
