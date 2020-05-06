from rest_framework import viewsets

from apps.core import models
from apps.api import serializers


class AuthorViewset(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
