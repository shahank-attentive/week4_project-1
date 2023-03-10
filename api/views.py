from django.shortcuts import render
from .models import User, Event
from .serializers import UserSerializer, EventSerializer
from rest_framework import viewsets, status
from django.db.models import Model
from django.http import JsonResponse
from rest_framework.response import Response
from django.db.models import Q
from datetime import datetime
from django.utils import timezone

# import django.utils import timezone

# Create your views here.


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EventModelViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    ordering_fields = ("time",)

    def get_queryset(self):
        user = self.request.query_params.get("user", None)
        filter_type = self.request.query_params.get("filter_type", None)
        if user == None:
            query_set = Event.objects.all()
        else:
            if filter_type == None:
                query_set = Event.objects.filter(
                    Q(organiser=user)
                    | Q(event_type="public")
                    | Q(users_invited__in=user)
                )

            elif filter_type == "myevents_future":
                query_set = Event.objects.filter(
                    (Q(organiser=user))
                    & Q(
                        # event_time_from__lte=timezone.now(),
                        event_time_from__gte=timezone.now(),
                    )
                )
            elif filter_type == "myevents_ongoing":
                query_set = Event.objects.filter(
                    (Q(organiser=user))
                    & Q(
                        event_time_from__lte=timezone.now(),
                        event_time_till__gte=timezone.now(),
                    )
                )
            elif filter_type == "myevents_past":
                query_set = Event.objects.filter(
                    (Q(organiser=user))
                    & Q(
                        # event_time_from__lte=timezone.now(),
                        event_time_till__lte=timezone.now(),
                    )
                )
            elif filter_type == "myevents_public":
                query_set = Event.objects.filter(
                    Q(organiser=user)
                    & Q(event_type="public")
                    # & Q(
                    #     event_time_from__lte=timezone.now(),
                    #     event_time_till__lte=timezone.now(),
                    # )
                )
            elif filter_type == "myevents_private":
                query_set = Event.objects.filter(
                    Q(organiser=user)
                    & Q(event_type="private")
                    # & Q(
                    #     # event_time_from__lte=timezone.now(),
                    #     event_time_till__lte=timezone.now(),
                    # )
                )

            elif filter_type == "future":
                query_set = Event.objects.filter(
                    (
                        Q(organiser=user)
                        | Q(event_type="public")
                        | Q(users_invited__in=user)
                    )
                    & Q(
                        # event_time_from__lte=timezone.now(),
                        event_time_from__gte=timezone.now(),
                    )
                )
            elif filter_type == "ongoing":
                query_set = Event.objects.filter(
                    (
                        Q(organiser=user)
                        | Q(event_type="public")
                        | Q(users_invited__in=user)
                    )
                    & Q(
                        event_time_from__lte=timezone.now(),
                        event_time_till__gte=timezone.now(),
                    )
                )
            elif filter_type == "invited":
                query_set = Event.objects.filter(
                    (Q(users_invited__in=user))
                    & Q(
                        # event_time_from__lte=timezone.now(),
                        event_time_till__gte=timezone.now(),
                    )
                )

            # print(type(organiser))

        return query_set.distinct()  # kuch duplicates hai

    def list(self, request):
        # print(datetime.now())
        # filter_type = self.request.query_params.get("filter_type", None)
        # if filter_type == None:
        query_set = self.get_queryset()
        # elif filter_type == "future":
        #     current_time = datetime.now()
        #     query_set = self.get_queryset().filter(time > current_time)

        data = EventSerializer(query_set, many=True, context={"request": request})
        return Response(data.data)

    def update(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance=instance,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        user = self.request.query_params.get("user", None)
        # print(type(instance.organiser.id))
        # print(user)
        if int(user) == instance.organiser.id:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({"msg": "error"})
        else:
            return Response({"msg": "user not allowed"})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user = self.request.query_params.get("user", None)
        if (
            int(user) == instance.organiser.id
            and instance.event_time_from > timezone.now()
        ):  # time condition remaining
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
