from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
import uuid

from mixins.models_mixins import PKMixin


class Category(PKMixin):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, help_text='Category name')
    description = models.CharField(max_length=255, default='Description', help_text='Category description')
    image = models.ImageField(upload_to='Images', default='default.jpg')


class Item(PKMixin):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text='Item name')
    description = models.CharField(max_length=255, default='Description', help_text='Item description')
    image = models.ImageField(upload_to='Images', default='default.jpg')


class Product(PKMixin):
    def __str__(self):
        return self.id

    price = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=255)
    items = models.ManyToManyField(Item)


class Discount(PKMixin):
    def __str__(self):
        return self.id

    amount = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    code = models.CharField(max_length=255, default='Code')
    is_active = models.BooleanField(default=True)
    discount_type = models.BooleanField(default=0)


class Order(PKMixin):
    products = models.ManyToManyField(Product)
    total_amount = models.PositiveIntegerField(default=0)
    user = models.ManyToManyField(User)
