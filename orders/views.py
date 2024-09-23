import json
from django.views import View
from django.views.generic import DetailView
from django.http import JsonResponse
from django.db.utils import IntegrityError

from products.models import Product
from orders.models import Cart, CartItem


class AddToCardView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            product = Product.objects.get(uid=data['product_uid'])
            cart, created = Cart.objects.get_or_create(owner=request.user)
            CartItem.objects.create(
                product=product,
                cart=cart,
                quantity=data['quantity']
            )
        except (Product.DoesNotExist, IntegrityError):
            return JsonResponse({
                'success': False,
                'message': "Erreur d'ajout au panier."
            })

        return JsonResponse({'success': True})


class CartOrderView(DetailView):
    model = Cart
    template_name = 'orders/cart_orders.html'
    context_object_name = 'cart'

    def get_object(self):
        return self.model.objects.get(owner=self.request.user)
