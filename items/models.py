from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from djStore.constants import MAX_DIGITS, DECIMAL_PLACES
from mixins.models_mixins import PKMixin, Description, Image


class Category(PKMixin, Description, Image):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, help_text='Category name')


class Item(PKMixin):
    def __str__(self):
        return f" {self.name} | {self.category} "

    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.id)])

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text='Item name')


class Product(PKMixin, Description, Image):
    def __str__(self):
        return f'{self.name} | {self.price}'

    name = models.CharField(max_length=255, help_text='Product name')
    price = models.DecimalField(max_digits=MAX_DIGITS,
                                decimal_places=DECIMAL_PLACES,
                                default=0)
    sku = models.CharField(max_length=255)
    items = models.ManyToManyField(Item)
