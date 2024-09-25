from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'price', 'quantity', 'is_seen', 'created_at'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
