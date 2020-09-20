from django.contrib import admin
from django.contrib.admin import register

from category.models import Category, CatAttribute


class CatAttributeInline(admin.TabularInline):
    model = CatAttribute


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (CatAttributeInline,)


class CatAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'id')


# admin.site.register(Category, CategoryAdmin)
admin.site.register(CatAttribute, CatAttributeAdmin)