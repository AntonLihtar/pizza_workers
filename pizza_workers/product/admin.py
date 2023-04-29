from django.contrib import admin
from django.db.models import QuerySet

from .models import Product


class PriceFilter(admin.SimpleListFilter):
    title = 'Показать по цене'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Меньше 10$'),
            ('10<50', 'От 10 до 50$'),
            ('50<100', 'От 50 до 100$'),
            ('<100', 'Все позиции до 100$'),
            ('>100', 'Все позиции от 100$'),
        ]

    def queryset(self, request, queryset: QuerySet):
        match self.value():
            case '<10':
                return queryset.filter(price__lt=10)
            case '10<50':
                return queryset.filter(price__lt=50).filter(price__gte=10)
            case '50<100':
                return queryset.filter(price__lt=100).filter(price__gte=50)
            case '<100':
                return queryset.filter(price__lt=100)
            case '>100':
                return queryset.filter(price__gte=100)
            case _:
                return queryset


class QuanFilter(admin.SimpleListFilter):
    title = 'Показать по количеству'
    parameter_name = 'quan'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Меньше 10 шт'),
            ('10<50', 'От 10 до 50 штук')
        ]

    def queryset(self, request, queryset: QuerySet):
        match self.value():
            case '<10':
                return queryset.filter(quantity__lt=10)
            case '10<50':
                return queryset.filter(quantity__lt=50).filter(quantity__gte=10)
            case _:
                return queryset


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'price', 'quantity', 'publish', 'doc']
    list_editable = ['price', 'quantity', 'publish']
    ordering = ['id']
    list_per_page = 20
    list_filter = [PriceFilter, QuanFilter, 'publish']
