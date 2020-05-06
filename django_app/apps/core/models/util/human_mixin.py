from django.db import models


class HumanMixin(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
