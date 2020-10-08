from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.models import BaseModel
from product.models import Product

User = get_user_model()


def create_user():
    user = User.objects.get_or_create('delete_account')[0]
    return user


class Basket(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='baskets', on_delete=models.SET(create_user))
    products = models.ManyToManyField(
        Product, verbose_name=_('product'), related_name='baskets', through='BasketProduct'
    )
    paid = models.BooleanField(verbose_name="paid", default=False)

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
        db_table = 'basket'

    def __str__(self):
        return "{} ({})".format(self.user.username, self.pk)

    def total_price(self):
        price = 0
        for product in self.basket_products.all():
            price += (product.price * product.quantity)
        return price


class BasketProduct(BaseModel):
    basket = models.ForeignKey(
        Basket, verbose_name=_('basket'), related_name='basket_products', on_delete=models.CASCADE
        )
    product = models.ForeignKey(
        Product, verbose_name=_('product'), related_name='basket_products', on_delete=models.CASCADE
    )
    quantity = models.PositiveSmallIntegerField(verbose_name=_('quantity'),)
    price = models.PositiveIntegerField(verbose_name=_('price'))

    class Meta:
        verbose_name = 'BasketProduct'
        verbose_name_plural = 'BasketProducts'
        db_table = 'basket_product'

    def __str__(self):
        return "{}({})".format(self.product.name, self.quantity)
