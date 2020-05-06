from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.core import models
from .author import AuthorSerializer


class BookWriteSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(slug_field='code', queryset=models.Language.objects_shown.all())

    class Meta:
        model = models.Book
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=models.Book.objects.all(),
                fields=['title', 'language', 'publish_year']
            )
        ]


class BookReadSerializer(BookWriteSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
