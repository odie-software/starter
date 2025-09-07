from rest_framework import serializers

from ..models import CustomUser


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("pk", "username", "role", "clients")
