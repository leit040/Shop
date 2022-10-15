from django.contrib import admin

from .models import Item, Category, Product


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at',)
    readonly_fields = ('image_preview',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sku', 'create_at',)
    filter_horizontal = ('items',)
    readonly_fields = ('image_preview',)
