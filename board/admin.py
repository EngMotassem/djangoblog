from board.models import Students, absent, absentstudent
from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin


# Register your models here.
#admin.site.unregister(absentstudent)
@admin.register(Students)
class StudentsAdmin(ImportExportModelAdmin):
    pass
#@admin.register(absentstudent)
#class absentStAdmin(ImportExportModelAdmin):
    #pass