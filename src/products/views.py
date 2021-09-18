from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product.html"
