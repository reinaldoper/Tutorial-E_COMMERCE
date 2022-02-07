from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.db.models import Q

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        #SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kargs):
        request = self.request
        result = request.GET
        query = result.get('q',  None) # method['q']
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()