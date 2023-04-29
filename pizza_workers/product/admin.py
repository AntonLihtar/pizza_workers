from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'price', 'quantity', 'doc']
    list_editable = ['price', 'quantity']
    ordering = ['id']
    