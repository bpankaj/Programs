# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Invoice, Transaction


class InvoiceAdmin(admin.ModelAdmin):
	fields = ['customer', 'date', 'total_quantity', 'total_amount']
	list_display = ('customer', 'date', 'total_quantity', 'total_amount')
	list_filter = ['date']
	search_fields = ['customer']


class TransactionAdmin(admin.ModelAdmin):
	fields = ['product', 'quantity', 'price', 'line_total']
	list_display = ('product', 'quantity', 'price', 'line_total')
	search_fields = ['product']


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Transaction, TransactionAdmin)
