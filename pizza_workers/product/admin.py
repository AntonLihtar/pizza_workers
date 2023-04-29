from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'price', 'quantity', 'publish', 'doc']
    list_editable = ['price', 'quantity', 'publish']
    ordering = ['id']
    list_per_page = 20
