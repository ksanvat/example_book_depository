from rest_framework import viewsets

from apps.core import models
from apps.api import serializers


class LanguagesViewset(viewsets.ModelViewSet):
    queryset = models.Language.objects_shown.all()
    serializer_class = serializers.LanguageSerializer
