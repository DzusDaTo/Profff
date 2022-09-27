from django.contrib import admin
from .models import Resumeout
from import_export.admin import ImportExportModelAdmin


class BbAdmin(ImportExportModelAdmin):
    list_display = ('special', 'date', 'number')
    search_fields = ('special', 'date', 'number')


admin.site.register(Resumeout, BbAdmin)
