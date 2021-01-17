from django.db import models
from core.validators import validate_code

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, validators=[validate_code])

    class Meta:
        abstract = True
