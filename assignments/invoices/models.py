# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Invoice(models.Model):
	customer = models.CharField(max_length=200)
	date = models.DateTimeField(blank=True, null=True)
	total_quantity = models.IntegerField(default=0)
	total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return self.customer


@python_2_unicode_compatible
class Transaction(models.Model):
	invoice = models.ForeignKey(Invoice, null=True, blank=True)
	product = models.CharField(max_length=200)
	quantity = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	line_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return self.product