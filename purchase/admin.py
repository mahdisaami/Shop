from django.contrib import admin

from product.models import Product
from purchase.models import Basket, BasketProduct


class BasketProductAdminInline(admin.TabularInline):
    model = BasketProduct


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'custom_column', 'invoice', 'paid')
    inlines = (BasketProductAdminInline,)

    def custom_column(self, obj):
        return ', '.join(obj.product.value_list('name', flat=True))

    custom_column.short_description = 'Product'


class BasketProductAdmin(admin.ModelAdmin):
    list_display = ('basket', 'product', 'quantity', 'price')


admin.site.register(Basket, BasketAdmin)
admin.site.register(BasketProduct, BasketProductAdmin)