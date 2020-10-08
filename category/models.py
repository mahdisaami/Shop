from django.db import models
from django.utils.translation import ugettext_lazy as _

from lib.models import BaseModel


class Category(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=32)
    categories = models.ForeignKey(
        'self', verbose_name=_('categories'), related_name='category',
        max_length=32, on_delete=models.SET_NULL, null=True, blank=True)
    is_parent = models.BooleanField(verbose_name=_('is_parent'), default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'

    def __str__(self):
        return self.name


class CatAttribute(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=32)
    category = models.ForeignKey(
        Category, verbose_name=_('category'), related_name='cat_attributes', on_delete=models.CASCADE
    )


    class Meta:
        verbose_name = 'CatAttribute'
        verbose_name_plural = 'CatAttributes'
        db_table = 'cat_attribute'

    def __str__(self):
        return f'{self.category.name}: ({self.name})'
