from django.contrib import admin

from orders.models import Discount, Order

admin.site.register(Discount)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...
