from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=200)
    email_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    event_name = models.CharField(max_length=300)
    event_time_from = models.DateTimeField(default=datetime.now())
    event_time_till = models.DateTimeField()
    event_type = models.CharField(max_length=100)
    organiser = models.ForeignKey(
        User, related_name="organiser", null=False, on_delete=models.CASCADE
    )
    users_invited = models.ManyToManyField(
        User, blank=True, related_name="users_invited"
    )

    # class Meta:
    #     unique_together = (id,)

    def __str__(self):
        return self.name
