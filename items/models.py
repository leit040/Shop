from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
import uuid

from django.utils.safestring import mark_safe

from mixins.models_mixins import PKMixin


class Category(PKMixin):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, help_text='Category name')
    description = models.CharField(max_length=255, default='Description', help_text='Category description')
    image = models.ImageField(upload_to='Images', default='default.jpg')


class Item(PKMixin):
    def __str__(self):
        return f" {self.name} | {self.category} "

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text='Item name')
    description = models.CharField(max_length=255, default='Description', help_text='Item description')
    image = models.ImageField(upload_to='Images', default='default.jpg')

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""


class Product(PKMixin):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, help_text='Product name')
    price = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=255)
    items = models.ManyToManyField(Item)


