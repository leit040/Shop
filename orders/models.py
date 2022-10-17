from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum
from djStore.model_choices import DiscountTypes
from items.models import Product
from mixins.models_mixins import PKMixin, Description, UserModel


class Discount(PKMixin, Description):
    def __str__(self):
        return self.code

    amount = models.PositiveIntegerField(default=1,
                                         validators=[MinValueValidator(1)])
    code = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    discount_type = models.SmallIntegerField(DiscountTypes.choices,
                                             default=DiscountTypes.VALUE)


class Order(PKMixin, UserModel):
    def __str__(self):
        return f' {self.user} | {self.create_at}'

    products = models.ManyToManyField(Product)
    discount = models.ForeignKey(Discount,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    def getTotalAmount(self):
        amount = self.products.aggregate(sum=Sum('price')).get('sum')
        order_discount = self.discount
        if order_discount:
            if order_discount.discount_type == 0:
                return amount - order_discount.amount
            else:
                return amount - (amount / 100 * order_discount.amount)
        return amount
