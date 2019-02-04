from django.contrib import admin

from core.models import DataFile


@admin.register(DataFile)
class DataFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_added')
    list_filter = ('date_added',)
