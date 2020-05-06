from django.db import models

from .util import HumanMixin, AutoUUIDField


class Subscriber(HumanMixin):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['last_name', 'first_name', 'middle_name', 'email'], name='unique_subscriber')
        ]

    id = AutoUUIDField(primary_key=True)
    email = models.EmailField()
