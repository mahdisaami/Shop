from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.models import BaseModel


User = get_user_model()


class Profile(BaseModel):
    user = models.OneToOneField(User, verbose_name=_('user'), related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user/avatar/', verbose_name=_('avatar'), null=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'profile'

    def __str__(self):
        return self.user.username
