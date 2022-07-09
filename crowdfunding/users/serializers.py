from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=5000)
    profile_image = serializers.URLField()
    password = serializers.CharField(style={'input_type': 'password'})

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return CustomUser.objects.create(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):

        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_image = validated_data.get('profile image',instance.profile_image)
        instance.password = make_password((validated_data.get('password')))
        instance.save()
        return instance