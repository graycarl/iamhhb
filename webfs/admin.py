from django.contrib import admin

# Register your models here.
from .models import WebFile


class WebFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'size', 'created_at')
    fields = ('file', 'mimetype', 'size')
    readonly_fields = ('mimetype', 'size')


admin.site.register(WebFile, WebFileAdmin)
