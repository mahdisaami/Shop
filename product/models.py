from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import FileExtensionValidator

from category.models import Category, CatAttribute
from lib.models import BaseModel


User = get_user_model()


class Product(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=32)
    price = models.FloatField(verbose_name=_('price'), )
    description = models.TextField(verbose_name=_('description'), null=True)
    category = models.ForeignKey(
        Category, verbose_name=_('category'), related_name='products', on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='products', on_delete=models.CASCADE)
    available = models.BooleanField(verbose_name=_('available'), default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"
        db_table = 'product'

    def __str__(self):
        return self.name


class PrAttribute(BaseModel):
    name = models.ForeignKey(
        CatAttribute, verbose_name=_('name'), related_name='pr_attributes', on_delete=models.CASCADE
        )
    product = models.ForeignKey(
        Product, verbose_name=_('product'), related_name='pr_attribute', on_delete=models.CASCADE
        )
    value = models.CharField(verbose_name=_('value'), max_length=32)

    class Meta:
        verbose_name = 'PrAttribute'
        verbose_name_plural = 'PrAttributes'
        db_table = 'pr_attribute'

    def __str__(self):
        return f"{self.name.name}: {self.value}"


class Media(BaseModel):
    IMAGE = 0
    VIDEO = 1

    MEDIA_TYPE = (
        (IMAGE, 'image'),
        (VIDEO, 'video'),
    )

    media_type = models.PositiveSmallIntegerField(verbose_name=_('media type'), choices=MEDIA_TYPE, default=0)
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='medias', on_delete=models.CASCADE)
    media_file = models.FileField(
        verbose_name=_('media file'), upload_to='content/media',
        validators=[FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'mp4', 'wmv', 'flv', 'png'))]
    )

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'
        db_table = 'media'

    def __str__(self):
        return '{} - {}'.format(str(self.product), self.get_media_type_display())


class Star(BaseModel):
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='stars', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='stars', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'
        db_table = 'star'

    def __str__(self):
        return f'{self.user.username} >> {self.product.name}'


class Comment(BaseModel):
    text = models.TextField(verbose_name=_('text'))
    product = models.ForeignKey(Product, verbose_name=_('product'), related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='comments', on_delete=models.CASCADE)
    reply_to = models.ForeignKey(
        'self', verbose_name=_('reply to'), related_name='replies', on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comment'

    def __str__(self):
        return f'{self.user.username} >> {self.product.name}'