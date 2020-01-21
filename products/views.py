from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset      = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductListView(ListView):
    template_name = "products/list.html"
    # queryset = Product.objects.all()
    # câu lệnh tìm tên gần đúng field 
    # qs = Product.objects.filter(description__contains='2')

    # def get_context_data(self, *args, **kwargs):
    #   # https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
    #   # https://www.howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python--packing-va-unpacking-arguments-2655
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

class ProductDeatailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found....")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmmm")
        return instance


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        # https://www.geeksforgeeks.org/packing-and-unpacking-arguments-in-python/
        # https://www.howkteam.vn/course/lap-trinh-python-co-ban/kieu-du-lieu-function-trong-python--packing-va-unpacking-arguments-2655
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)



# get_context_data(abc, 123, adsfads, another=abc, abc=123)

def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk, featured=True) #id
    # instance = get_object_or_404(Product, pk=pk, featured=True) #id

    # try:
    #     instance = Product.objects.get(id=pk) #id
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")
    
    instance = product.object.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    # print(instance)
    # qs = Product.object.filter(id=pk)
    # print(qs)
    # if qs.exists() and qs.count() == 1: # len(qs)
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)