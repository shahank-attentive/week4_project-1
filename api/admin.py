from django.contrib import admin

# Register your models here.
from .models import User, Event


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email_id"]


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
