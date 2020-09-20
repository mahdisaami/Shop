from django.contrib import admin

from product.models import PrAttribute, Product, Media, Star, Comment


class PrAttributeInline(admin.TabularInline):
    model = PrAttribute


class MediaInline(admin.TabularInline):
    model = Media


class PrAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'available')
    inlines = (PrAttributeInline, MediaInline)


admin.site.register(Product, ProductAdmin)
admin.site.register(Star)
admin.site.register(Comment)
admin.site.register(PrAttribute, PrAttributeAdmin)