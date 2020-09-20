from datetime import datetime

from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(verbose_name='created time', auto_now_add=datetime.now())
    modified_time = models.DateTimeField(verbose_name='created time', auto_now=datetime.now())

    class Meta:
        abstract = True
