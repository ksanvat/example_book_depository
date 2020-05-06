from django.db.models import Count
from rest_framework import viewsets, mixins

from apps.api import serializers
from apps.core import models
from . import util


class SearchViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    search_fields = ['authors_count']
    filter_backends = (util.SearchCountFilter,)
    queryset = models.Book.objects.prefetch_related('authors').annotate(authors_count=Count('authors')).all()
    serializer_class = serializers.BookReadSerializer
