import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.models import BaseModel
from purchase.models import Basket

User = get_user_model()


def create_user():
    user = User.objects.get_or_create('delete_account')[0]
    return user


class Invoice(BaseModel):
    uuid = models.UUIDField(verbose_name=_('uuid'), unique=True, default=uuid.uuid4, editable=False)
    price = models.PositiveIntegerField(verbose_name=_('price'))
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='invoices', on_delete=models.SET(create_user))
    paid = models.BooleanField(verbose_name=_('paid'), default=False)
    basket = models.OneToOneField(
        Basket, verbose_name=_('basket'), related_name='invoice', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        db_table = 'invoice'

    def __str__(self):
        return "{}: {}".format(self.uuid, self.paid)
