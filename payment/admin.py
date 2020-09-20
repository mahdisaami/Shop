from django.contrib import admin

from payment.models import Invoice


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('user', 'paid', 'price')


admin.site.register(Invoice, InvoiceAdmin)
