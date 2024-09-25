from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import F

from .models import Product


class ProductView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return self.model.objects.select_related(
            'category'
        ).filter(is_seen=True).annotate(
            reduce_price=F('price')-F('price')*0.1
        ).order_by('created_at')


class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'uid'

    def get_object(self):
        return Product.objects.get(uid=self.kwargs.get('uid'))
