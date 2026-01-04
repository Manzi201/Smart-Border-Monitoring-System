from django.db import models
import uuid

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=50, unique=True)
    place_of_birth = models.CharField(max_length=255)
    current_living_location = models.CharField(max_length=255)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.national_id})"

class GaitProfile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='gait_profile')
    gait_data = models.JSONField(help_text="Stored gait features or raw signal references")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gait Profile for {self.person.full_name}"

class CrossingEvent(models.Model):
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, related_name='crossings')
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_identified = models.BooleanField(default=False)
    raw_gait_data = models.JSONField(null=True, blank=True)
    confidence_score = models.FloatField(default=0.0)

    def __str__(self):
        status = "Identified" if self.is_identified else "Unknown"
        return f"Crossing at {self.location} - {status} at {self.timestamp}"
