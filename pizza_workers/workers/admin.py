from django.contrib import admin

from .models import Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'name',
                    'last_name', 'surname',
                    'telephone', 'sex', 'age',
                    'experience', 'doc', 'salary']

    list_editable = ['title', 'name',
                     'last_name', 'surname',
                     'telephone', 'sex', 'age',
                     'experience', 'doc', 'salary']
