from django.db import models
from core.models import TimeStampedModel
from django.utils import timezone

class PublishedQuerySet(models.QuerySet):
    def published(self, **kwargs):
        return self.filter(created__lte=timezone.now(), **kwargs)

    def test(self):
        return self.filter(title='test')

# class PublishedManger(models.Manager):

#     use_for_related_fields = True

#     def published(self, **kwargs):
#         return self.filter(created__lte=timezone.now(), **kwargs)

#     def test(self):
#         return self.filter(title='test')

class Flavor(TimeStampedModel):
    body = models.TextField(blank = True)

    objects = PublishedQuerySet().as_manager()