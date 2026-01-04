from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, GaitProfileViewSet, CrossingEventViewSet

router = DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'gait-profiles', GaitProfileViewSet)
router.register(r'crossings', CrossingEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
