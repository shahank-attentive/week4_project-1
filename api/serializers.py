from rest_framework import serializers
from .models import User, Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]


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

    # def create(self, validated_data):
    #     data = validated_data.get("users_invited")
    #     if sizeof(data) == 0:
    #         validated_data.pop("users_invited")
    #     # print("data", type(data))  # data is list of dict
    #     # print("to print", data)
    #     device = Event.objects.create(**validated_data)
    #     # for a in data:  # fetching the list
    #     #     Event.objects.create(device=device, **a)
