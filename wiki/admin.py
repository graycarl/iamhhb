from django.contrib import admin
from .models import Page, Tag


class PageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'visit_count', 'created_at')
    fields = ('slug', 'title', 'content', 'tags', 'visit_count')
    readonly_fields = ('visit_count', 'visit_last_at')


class TagAdmin(admin.ModelAdmin):
    list_display = ('slug', 'text', 'page_count', 'created_at')
    fields = ('slug', 'text')


admin.site.register(Page, PageAdmin)
admin.site.register(Tag, TagAdmin)
