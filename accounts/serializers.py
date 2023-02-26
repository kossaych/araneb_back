from django.contrib.auth.models import User
from rest_framework import serializers
from .models import*

class RegisterSerializer(serializers.Serializer):
    class Meta:
        fields = fields =["username", "email", "password1", "password2"]

    def create(self, validated_data):
        return User.objects.create(**validated_data)