from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import MainUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}


class ProfileSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(write_only=True)
    avatar = serializers.ImageField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+777777777777'. Up to 15 " +
                                         "digits allowed.")
    phone_number = serializers.CharField(max_length=17, validators=[phone_regex])

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance
