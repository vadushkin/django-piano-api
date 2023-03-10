from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class SheetAdminModel(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "user",
        "author",
        "description",
        "file_pdf",
        "get_photo",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name", "description")
    fields = (
        "name",
        "description",
        "file_pdf",
        "get_photo",
        "user",
        "author",
        "category",
        "tags",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("get_photo", "created_at", "updated_at")

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo}" width="100">')
        else:
            return "Photo doesn't exist"


class TagAdminModel(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "user",
    )
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdminModel(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "user",
    )
    prepopulated_fields = {"slug": ("name",)}


class AuthorAdminModel(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "user",
    )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Sheet, SheetAdminModel)
admin.site.register(models.Author, AuthorAdminModel)
admin.site.register(models.Tag, TagAdminModel)
admin.site.register(models.Category, CategoryAdminModel)
