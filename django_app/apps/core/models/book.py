from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.service import notify_subscribers
from .util import AutoUUIDField
from .author import Author
from .language import Language


class Book(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'language', 'publish_year'], name='unique_book')
        ]

    id = AutoUUIDField(primary_key=True)
    title = models.CharField(max_length=255)
    language = models.ForeignKey(to=Language, on_delete=models.CASCADE)
    publish_year = models.IntegerField()
    authors = models.ManyToManyField(to=Author)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Book)
def on_create_book(sender, instance, created, **kwargs):
    if created:
        notify_subscribers.new_book(instance)
