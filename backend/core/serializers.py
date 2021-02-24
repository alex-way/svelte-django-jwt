from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Example


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ["name"]
