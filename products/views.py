from dataclasses import fields
from pipes import Template
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import render
from django.http import Http404
from .models import Product

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"
    
    def get_queryset(self, *args, **kwargs):
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all()
    template_name = "products/list.html"
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product, slug = slug, active = True)
        try:
            instance = Product.objects.get(slug = slug, active = True)
        except Product.DoesNotExist:
            raise Http404("Não encontrado!")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug = slug, active = True)
            instance =  qs.first()
        return instance

#Class Based View
class ProductDetailView(DetailView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    #queryset = Product.objects.all()
    template_name = "products/detail.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Esse produto não existe!")
        return instance

class ProductCreatView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/create.html'
    success_url = '/'
        
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url ="/"