# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def list_product(request):
	products = Product.objects.all()
	return render(request, 'products/products.html', {'products': products})


def create_product(request):
	form = ProductForm(request.POST or None)
	if form and form.is_valid():
		form.save()
		return HttpResponseRedirect("/products/")
	return render(request, "products/product_forms.html", {'form': form})


def update_product(request, id):
	product = Product.objects.get(id=id)
	form = ProductForm(request.POST or None, instance=product)
	if form and form.is_valid():
		form.save()
		return HttpResponseRedirect("/products/")
	return render(request, "products/product_forms.html", {"form": form, "product": product})


def delete_product(request, id):
	product = Product.objects.get(id=id)
	if request.method == "POST":
		product.delete()
		return HttpResponseRedirect("/products/")
	return render(request, "products/confirm_delete.html", {'product': product})

