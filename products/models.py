import uuid
from django.db import models
from django.utils import timezone
from django.db.models import F


class Category(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, null=True)
    name = models.CharField(
        max_length=100, verbose_name='Nom de la categorie'
    )
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Date d'ajout"
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name='products'
    )
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.quantity}"

    class Meta:
        indexes = [
            models.Index(fields=['is_seen', 'price']),
            models.Index(F('quantity')*F('price'), name='tatal_amount_idx'),
            models.Index(F('price')-F('price')*0.1, name='tatal_amount_idx2'),
        ]
