from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.models import BaseModel

User = get_user_model()


def create_user():
    user = User.objects.get_or_create('delete_account')[0]
    return user


class Invoice(BaseModel):
    uuid = models.UUIDField(verbose_name=_('uuid'), unique=True)
    price = models.PositiveIntegerField(verbose_name=_('price'))
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='invoices', on_delete=models.SET(create_user))
    paid = models.BooleanField(verbose_name=_('paid'))

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        db_table = 'invoice'

    def __str__(self):
        return str(self.uuid), self.paid
