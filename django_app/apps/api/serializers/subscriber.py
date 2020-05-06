from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from apps.core import models


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscriber
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=models.Subscriber.objects.all(),
                fields=['last_name', 'first_name', 'middle_name', 'email']
            )
        ]
