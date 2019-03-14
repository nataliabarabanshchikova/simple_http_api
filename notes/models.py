import uuid

from django.db import models
from django.utils import timezone


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=256)
    text = models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.date_update = timezone.now()
        super(Note, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
