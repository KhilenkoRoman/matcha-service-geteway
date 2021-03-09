from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from apps.users.models import User, UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('gender', 'birth_date')


class UserSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'user_info', )


class UserCreateSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer()
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        user_info = validated_data.pop('user_info')
        obj = User.objects.create_user(**validated_data)
        user_info['user'] = obj
        UserInfo.objects.create(**user_info)
        return obj

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'user_info', 'token')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
