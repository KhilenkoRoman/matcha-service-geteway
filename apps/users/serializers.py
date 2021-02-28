from django.conf import settings
from django.conf import settings
from rest_framework import serializers
from django.conf import settings
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')