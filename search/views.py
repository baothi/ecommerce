from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404

from products.models import Product
# Create your views here.
class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = request.GET.get('q', None) # method_dict['q'] "Sản"
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
        # return Product.objects.filter(title__iexact="Sản")
        '''
           __icontains = field contains this
           __iexact = fields is exctly this

        '''