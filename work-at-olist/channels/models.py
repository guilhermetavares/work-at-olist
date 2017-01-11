from __future__ import unicode_literals

import uuid

from django.utils.timezone import now
from django.db import models

from mptt.models import MPTTModel, TreeForeignKey
from mptt.templatetags.mptt_tags import cache_tree_children

from utils.mptt_utils import recursive_mptt_to_dict


class Channel(models.Model):
    name = models.CharField(u'nome', max_length=64)
    is_active = models.BooleanField(default=True)

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(u'criado em', default=now)

    def __str__(self):
        return self.name

    @property
    def categories_tree(self):
        from channels.serializers import ChannelCategorySerializer
        queryset = cache_tree_children(self.categories.all())
        categories = []
        for category in queryset:
            categories.append(recursive_mptt_to_dict(category, ChannelCategorySerializer))
        return categories


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

    @property
    def get_parent(self):
        if self.parent:
            return {
                'name': self.parent.name,
                'uuid': self.parent.uuid,
            }

    def __str__(self):
        return self.name