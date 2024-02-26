from rest_framework.serializers import ModelSerializer

from src.apps.user.models import UserModel


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('usr_username', 'usr_email', 'password', 'usr_created_at', 'usr_updated_at', 'usr_is_active', 'usr_is_admin')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True, 'style': {'input_type': 'password'}}
        }

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            usr_username=validated_data['usr_username'],
            usr_email=validated_data['usr_email'],
            usr_password=validated_data['password']
        )
        return user

    def update(self, instance: UserModel, validated_data):
        instance.usr_username = validated_data.get('usr_username', instance.usr_username)
        instance.usr_email = validated_data.get('usr_email', instance.usr_email)
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        return instance
