from django.contrib import admin
from .models import Driver, Doc, Car, Garage

admin.site.register(Doc)
admin.site.register(Garage)
admin.site.register(Driver)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'document', 'garage']
    list_editable = ['document', 'garage']
    filter_horizontal = ['drivers']
