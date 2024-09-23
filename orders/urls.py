from django.urls import path

from .views import AddToCardView, CartOrderView


urlpatterns = [
    path('carts', AddToCardView.as_view(), name='add_to_cart'),
    path('carts/orders', CartOrderView.as_view(), name='list_cart_orders'),
]
