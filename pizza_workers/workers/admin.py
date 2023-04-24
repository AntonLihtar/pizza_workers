from django.contrib import admin
from django.db.models import QuerySet

from .models import Worker


class AgeFilter(admin.SimpleListFilter):
    title = 'Возраст'
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return [
            ('<30', 'До 30 лет'),
            ('30<50', 'От 30 до 50 лет'),
            ('50>', 'Больше 50'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<30':
            return queryset.filter(age__lt=30)
        if self.value() == '30<50':
            return queryset.filter(age__gte=30).filter(age__lt=50)
        if self.value() == '50>':
            return queryset.filter(age__gte=50)
        return queryset


class SalaryFilter(admin.SimpleListFilter):
    title = 'зарплата'
    parameter_name = 'salary'

    def lookups(self, request, model_admin):
        return [
            ('<25', 'До 25к'),
            ('25<50', 'от 25к до 50к'),
            ('50>', 'От 50к'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<25':
            return queryset.filter(salary__lt=25000)
        if self.value() == '25<50':
            return queryset.filter(salary__gte=25000).filter(salary__lt=50000)
        if self.value() == '50>':
            return queryset.filter(salary__gte=50000)
        return queryset


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'name',
                    'last_name', 'surname',
                    'telephone', 'sex', 'age',
                    'experience', 'salary']

    list_editable = ['title', 'name',
                     'last_name', 'surname',
                     'telephone', 'sex', 'age',
                     'experience', 'salary']

    ordering = ['id']
    list_per_page = 5

    list_filter = ['sex', AgeFilter, 'experience', SalaryFilter]

    search_fields = ['name', 'surname']

