# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Product(models.Model):
	description = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	quantity = models.IntegerField()

	def __str__(self):
		return self.description