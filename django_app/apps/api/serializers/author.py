from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.core import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=models.Author.objects.all(),
                fields=['last_name', 'first_name', 'middle_name']
            )
        ]
