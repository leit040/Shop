import uuid
from datetime import datetime

from django.db import models


class PKMixin(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text="Unique ID",
                          editable=False)
    create_at = models.DateTimeField(default=datetime.now(),
                                     blank=True)
    update_at = models.DateTimeField(default=datetime.now(),
                                     blank=True)
    description = models.CharField(max_length=255,
                                   default='Description',
                                   help_text='Description')

    class Meta:
        abstract = True
