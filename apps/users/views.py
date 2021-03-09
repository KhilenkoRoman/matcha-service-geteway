from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .serializers import UserSerializer, UserCreateSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class RegistrationView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserCreateSerializer
