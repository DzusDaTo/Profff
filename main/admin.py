from django.contrib import admin
from .models import Shipment
from import_export.admin import ImportExportModelAdmin


class BbAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'published', 'school')
    search_fields = ('published', 'first_name', 'school')


admin.site.register(Shipment, BbAdmin)



