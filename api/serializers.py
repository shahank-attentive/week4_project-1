from rest_framework import serializers
from .models import User, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "is_staff"]
        extra_kwargs = {"password": {"write_only": True}}


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event

        fields = [
            "id",
            "event_name",
            "event_type",
            "event_time_from",
            "event_time_till",
            "organiser",
            "users_invited",
        ]
        read_only_fields = ("organiser",)
