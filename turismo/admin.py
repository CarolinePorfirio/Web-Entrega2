from django.contrib import admin
from .models import Package

# Register your models here.
class PackageAdmin (admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
admin.site.register(Package,PackageAdmin)

