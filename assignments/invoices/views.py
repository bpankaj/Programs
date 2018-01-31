# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from .models import Invoice, Transaction
import json
import datetime


@ensure_csrf_cookie
@csrf_exempt
def invoices(request, id=None):
	if request.method == "GET":
		if not id:
			invoice_data = Invoice.objects.all()
		else:
			invoice_data = Invoice.objects.filter(id=id)
		final_result = []
		if not invoice_data:
			final_result.append({"status_code": 100, "message": "Invoice is empty please create invoice "
								"and transactions"})
		for invoice in invoice_data:
			ret_dict = {}
			ret_dict['id'] = invoice.id
			ret_dict['customer'] = invoice.customer
			ret_dict['total_quantity'] = invoice.total_quantity
			ret_dict['total_amount'] = str(invoice.total_amount)
			ret_dict['date'] = str(invoice.date.date())
			ret_dict['transactions'] = list(invoice.transaction_set.all().values('id', 'product', 'quantity',
																		'price', 'line_total'))
			final_result.append(ret_dict)
		return JsonResponse(final_result, safe=False)

	if request.method == 'POST':
		try:
			invoice_data = json.loads(request.POST['invoice_data'])
		except Exception as e:
			return JsonResponse({'status_code': 100, 'message': 'Error while loading JSON data. Error is: %s' % e})
		customer = invoice_data.get('customer')
		transactions = invoice_data.get('transactions')
		# Creating the invoice and transactions
		if not id:
			total_amount = 0
			total_quantity = 0
			date = datetime.datetime.now()
			for tr in transactions:
				tr['line_total'] = tr['price'] * tr['quantity']
				total_amount += tr['line_total']
				total_quantity += tr['quantity']
			obj, success = Invoice.objects.get_or_create(customer=customer, date=date,
														total_quantity=total_quantity, total_amount=total_amount)
			for tr in transactions:
				obj.transaction_set.create(**tr)

			return JsonResponse({"status_code": 200, "message": "Invoice created successfully"})

		# Updating the invoice and transactions
		else:
			total_amount = 0
			total_quantity = 0
			invoice = Invoice.objects.get(id=id)
			transaction_data = invoice.transaction_set.all()
			if not transactions:
				if transaction_data:
					transaction_data.delete()
			else:
				if not transaction_data:
					for tr in transactions:
						tr['line_total'] = tr['price'] * tr['quantity']
						total_amount += tr['line_total']
						total_quantity += tr['quantity']
						invoice.transaction_set.create(**tr)
					Invoice.objects.filter(id=id).update(customer=customer, total_quantity=total_quantity,
														total_amount=total_amount)
				else:
					for tr in transactions:
						tr['line_total'] = tr['price'] * tr['quantity']
						total_amount += tr['line_total']
						total_quantity += tr['quantity']
					Invoice.objects.filter(id=id).update(customer=customer, total_quantity=total_quantity,
														total_amount=total_amount)
					for tr in transactions:
						invoice.transaction_set.update(**tr)

		return JsonResponse({"status_code": 200, "message": "Invoice updated successfully"})

	# Delete the invoice
	if request.method == 'DELETE':
		if id:
			invoice = Invoice.objects.get(id=id)
			invoice.transaction_set.all().delete()
			invoice.delete()
			return JsonResponse({"status_code": 200, "message": "Invoice deleted successfully"})
		return JsonResponse({"status_code": 100, "message": "Id was not given"})

