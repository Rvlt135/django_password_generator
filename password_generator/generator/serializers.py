from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from generator.models import PasswordsUserList


class ListPasswordUserSerializer(ModelSerializer):
    class Meta:
        model = PasswordsUserList
        fields = "__all__"


class PasswordCreateSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=30)
    resource = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return PasswordsUserList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.resource = validated_data.get('resource', instance.resource)
        instance.name = validated_data.get('name', instance.resource)
        instance.password = validated_data.get('password', instance.resource)
        instance.description = validated_data.get('description', instance.resource)
        instance.save()
        return instance
