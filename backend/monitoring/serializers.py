from rest_framework import serializers
from .models import Person, GaitProfile, CrossingEvent

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class GaitProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GaitProfile
        fields = '__all__'

class CrossingEventSerializer(serializers.ModelSerializer):
    person_name = serializers.ReadOnlyField(source='person.full_name')

    class Meta:
        model = CrossingEvent
        fields = '__all__'
