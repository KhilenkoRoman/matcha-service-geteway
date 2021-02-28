# Create your views here.
from .serializers import UserSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class GenericLeasesView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):

        return Response(data='data', status=status.HTTP_200_OK)