import uuid
from django.db import models
from django.utils import timezone
from django.db.models import Sum, F


class Cart(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    owner = models.OneToOneField(
        'users.User', on_delete=models.CASCADE, related_name='cart'
    )
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def amount(self):
        return self.items.aggregate(
            total_amont=Sum(F('quantity')*F('product__price'))
        )['total_amont']

    @property
    def nb_cart_items(self):
        return self.items.count()



class CartItem(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey(
        'Cart', on_delete=models.CASCADE, related_name='items',
    )
    quantity = models.IntegerField()

    class Meta:
        unique_together = ['product', 'cart']
