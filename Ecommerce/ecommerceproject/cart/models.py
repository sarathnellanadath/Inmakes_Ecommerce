from django.db import models
from shop.models import product


# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=250)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'cart_id'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)


class CartItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    QUANTITY = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.QUANTITY

    def __str__(self):
        return '{}'.format(self.product)
