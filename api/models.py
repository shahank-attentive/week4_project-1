from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

choice_type = (
    ("public", "Public"),
    ("private", "Private"),
)


class Event(models.Model):
    event_name = models.CharField(max_length=300)
    event_time_from = models.DateTimeField(default=datetime.now())
    event_time_till = models.DateTimeField()
    event_type = models.CharField(max_length=20, choices=choice_type, default="public")
    organiser = models.ForeignKey(
        User, related_name="organiser", null=True, blank=True, on_delete=models.CASCADE
    )
    users_invited = models.ManyToManyField(
        User, blank=True, related_name="users_invited"
    )

    def __str__(self):
        return self.event_name
