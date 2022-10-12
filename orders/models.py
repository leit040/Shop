from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum

from djStore.constants import MAX_DIGITS, DECIMAL_PLACES
from djStore.model_choices import DiscountTypes
from items.models import Product
from mixins.models_mixins import PKMixin


class Discount(PKMixin):
    def __str__(self):
        return self.code

    amount = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    code = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    discount_type = models.SmallIntegerField(DiscountTypes.choices,
                                             default=DiscountTypes.VALUE)


class Order(PKMixin):
    def __str__(self):
        return f' {self.user} | {self.create_at}'

    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=MAX_DIGITS,
                                       decimal_places=DECIMAL_PLACES,
                                       default=0)
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)
    discount = models.ForeignKey(Discount,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    def getTotalAmount(self):
        amount = sum(self.products.all().aggregate(Sum('price')))
        order_discount = self.discount
        if order_discount:
            if order_discount.discount_type == 0:
                return amount - order_discount.amount
            else:
                return amount - (amount / 100 * order_discount.amount)
        return amount
