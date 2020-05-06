from django.db import models

from .util import AutoUUIDField


class LanguageShownManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(is_shown=False)


class Language(models.Model):
    class Meta:
        ordering = ('-is_main', 'name')

    id = AutoUUIDField(primary_key=True)
    code = models.CharField(max_length=3, unique=True, db_index=True)
    name = models.CharField(max_length=64, unique=True)
    is_shown = models.BooleanField()
    is_main = models.BooleanField()

    objects = models.Manager()
    objects_shown = LanguageShownManager()

    def __str__(self):
        return self.name
