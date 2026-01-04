from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Person, GaitProfile, CrossingEvent
from .serializers import PersonSerializer, GaitProfileSerializer, CrossingEventSerializer
import random # Mock for recognition logic

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class GaitProfileViewSet(viewsets.ModelViewSet):
    queryset = GaitProfile.objects.all()
    serializer_class = GaitProfileSerializer

class CrossingEventViewSet(viewsets.ModelViewSet):
    queryset = CrossingEvent.objects.all().order_by('-timestamp')
    serializer_class = CrossingEventSerializer

    @action(detail=False, methods=['post'])
    def identify(self, request):
        """
        Receives raw gait data from mmWave sensor and attempts to match with existing profiles.
        """
        raw_data = request.data.get('gait_data')
        location = request.data.get('location', 'Unknown Point')

        if not raw_data:
            return Response({"error": "No gait data provided"}, status=status.HTTP_400_BAD_REQUEST)

        # MOCK RECOGNITION LOGIC
        # In reality, this would process raw_data through an AI model
        profiles = GaitProfile.objects.all()
        identified_person = None
        confidence = 0.0

        if profiles.exists():
            # Mocking a match: 70% chance to match a random profile if any exist
            if random.random() < 0.7:
                profile = random.choice(profiles)
                identified_person = profile.person
                confidence = random.uniform(0.85, 0.99)
            else:
                confidence = random.uniform(0.1, 0.4)

        # Record the crossing event
        event = CrossingEvent.objects.create(
            person=identified_person,
            location=location,
            is_identified=True if identified_person else False,
            raw_gait_data=raw_data,
            confidence_score=confidence
        )

        return Response({
            "status": "Identified" if identified_person else "Unknown",
            "person": PersonSerializer(identified_person).data if identified_person else None,
            "confidence": confidence,
            "event_id": event.id,
            "location": location,
            "timestamp": event.timestamp
        })

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Returns analytics for the dashboard."""
        from django.utils import timezone
        from datetime import timedelta
        
        last_24h = timezone.now() - timedelta(hours=24)
        crossings = CrossingEvent.objects.filter(timestamp__gte=last_24h)
        
        return Response({
            "total_24h": crossings.count(),
            "identified_24h": crossings.filter(is_identified=True).count(),
            "unknown_24h": crossings.filter(is_identified=False).count(),
            "location_breakdown": {
                loc: crossings.filter(location=loc).count() 
                for loc in crossings.values_list('location', flat=True).distinct()
            }
        })
