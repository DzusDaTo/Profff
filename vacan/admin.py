from django.contrib import admin
from .models import Vacan
from import_export.admin import ImportExportModelAdmin


class BbAdmin(ImportExportModelAdmin):
    list_display = ('special', 'date', 'zp')
    search_fields = ('special', 'date', 'zp')


admin.site.register(Vacan, BbAdmin)