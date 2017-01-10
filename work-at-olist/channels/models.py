from __future__ import unicode_literals

import uuid

from django.utils.timezone import now
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Channel(models.Model):
    name = models.CharField(u'nome', max_length=64)
    is_active = models.BooleanField(default=True)

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(u'criado em', default=now)

    def __str__(self):
        return self.name


class ChannelCategory(MPTTModel):
    channel = models.ForeignKey(Channel, related_name='categories')
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True)
    name = models.CharField(u'nome', max_length=124)
    slug = models.SlugField(u'slug', max_length=124)

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(u'criado em', default=now)

    def __str__(self):
        return self.name