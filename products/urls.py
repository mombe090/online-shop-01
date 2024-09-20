from django.urls import path

from .views import ProductView
from .views import ProductDetailView


urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('produit/<str:uid>', ProductDetailView.as_view(), name='product_detail')
]
