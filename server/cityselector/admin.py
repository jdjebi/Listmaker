from django.contrib import admin
from .models import CsvFile 

@admin.register(CsvFile)
class CsvFileAdmin(admin.ModelAdmin):
	list_display = ('id','path','date_creation')