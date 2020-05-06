from django.db import models

from .util import HumanMixin, AutoUUIDField


class Author(HumanMixin):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['last_name', 'first_name', 'middle_name'], name='unique_author')
        ]

    id = AutoUUIDField(primary_key=True)
