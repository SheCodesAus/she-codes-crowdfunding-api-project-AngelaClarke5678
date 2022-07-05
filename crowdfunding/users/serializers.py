from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=5000)
    profile_image = serializers.URLField()

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_image = validated_data.get('profile image',instance.profile_image)
        instance.save()
        return instance