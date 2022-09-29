from django.db import models
from django.urls import reverse
import uuid


class Item(models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    name = models.CharField(max_length=255, help_text='Item name')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    create_at = models.DateTimeField
    update_at = models.DateTimeField
