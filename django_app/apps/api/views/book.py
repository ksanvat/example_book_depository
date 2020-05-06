from rest_framework import viewsets

from apps.core import models
from apps.api import serializers
from . import util


class BookViewset(util.ReadWriteSerializerMixin, viewsets.ModelViewSet):
    queryset = models.Book.objects.select_related('language').prefetch_related('authors')
    read_serializer_class = serializers.BookReadSerializer
    write_serializer_class = serializers.BookWriteSerializer
