from datetime import datetime

from django.db import models
from django.urls import reverse
import uuid


class Item(models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, help_text="Unique ID")
    name = models.CharField(max_length=255, help_text='Item name')
    description = models.CharField(max_length=255, default='Description', help_text='Item description')
    image = models.ImageField(upload_to='Images', default='default.jpg')
    create_at = models.DateTimeField(default=datetime.now(), blank=True)
    update_at = models.DateTimeField(default=datetime.now(), blank=True)


class Category(models.Model):
    def __str__(self):
        return self.name

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, help_text="Unique ID")
    name = models.CharField(max_length=255, help_text='Category name')
    description = models.CharField(max_length=255, default='Description', help_text='Category description')
    image = models.ImageField(upload_to='Images', default='default.jpg')
    create_at = models.DateTimeField(default=datetime.now(), blank=True)
    update_at = models.DateTimeField(default=datetime.now(), blank=True)


class Product(models.Model):
    def __str__(self):
        return self.id

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, help_text="Unique ID")
    price = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=255)


class Discount(models.Model):
    def __str__(self):
        return self.id

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, help_text="Unique ID")
    amount = models.PositiveIntegerField(default=1)
    code = models.CharField(max_length=255, default='Code')
    is_active = models.BooleanField(default=True)
    discount_type = models.BooleanField(default=0)
