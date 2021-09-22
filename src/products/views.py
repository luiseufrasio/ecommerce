from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product

class ProductFeaturedListView(ListView):
    queryset = Product.objects.all().featured()
    template_name = "products/list.html"

class ProductFeaturedDetailView(DetailView):
	queryset = Product.objects.all().featured()
	template_name = "products/featured-detail.html"

class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"

class ProductDetailSlugView(DetailView):
    model = Product
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
    	slug = self.kwargs.get('slug')
    	object = get_object_or_404(Product, slug=slug, active=True)
    	return object

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
    	pk = self.kwargs.get('pk')
    	object = Product.objects.get_by_id(pk)
    	if object is None:
    		raise Http404("Product doesn't exist")
    	return object