from django.contrib import admin
from .models import Desktop
from import_export.admin import ImportExportModelAdmin


@admin.register(Desktop)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('School', 'Class', 'published')
    search_fields = ('School', 'Class', 'published')
