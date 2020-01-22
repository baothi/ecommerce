from django.urls import path


from .views import (
        ProductListView, 
        # product_list_view, 
        # ProductDetailView, 
        ProductDeatailSlugView,
        # product_detail_view,
        # ProductFeaturedListView,
        # ProductFeaturedDetailView
        )

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDeatailSlugView.as_view(), name='detail'),
]
