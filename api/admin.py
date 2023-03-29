from django.contrib import admin
from .models import User, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "event_name",
        "event_type",
        "event_time_from",
        "event_time_till",
        "organiser",
    ]
