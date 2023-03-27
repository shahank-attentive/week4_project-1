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

    # def create(self, validated_data):
    #     return Event.objects.create(
    #         event_name=validated_data["event_name"],
    #         event_type=validated_data["event_type"],
    #         event_time_from=validated_data["event_time_from"],
    #         event_time_till=validated_data["event_time_till"],
    #         users_invited=validated_data["users_invited"],
    #     )
