from rest_framework import viewsets

from apps.core import models
from apps.api import serializers


class SubscriberViewset(viewsets.ModelViewSet):
    queryset = models.Subscriber.objects.all()
    serializer_class = serializers.SubscriberSerializer
