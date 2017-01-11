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
        from channels.serializers import SimpleChannelCategorySerializer
        queryset = cache_tree_children(self.categories.all())
        categories = []
        for category in queryset:
            categories.append(recursive_mptt_to_dict(category, SimpleChannelCategorySerializer))
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
    def childrens(self):
        from channels.serializers import SimpleChannelCategorySerializer
        childrens = []
        for children in self.get_children():
            childrens.append(recursive_mptt_to_dict(children, SimpleChannelCategorySerializer))
        return childrens

    @property
    def parents(self):
        if self.parent:
            from channels.serializers import SimpleChannelCategorySerializer
            return recursive_mptt_to_dict(self.parent, SimpleChannelCategorySerializer, 'get_ancestors', 'parents')

    @property
    def channel_dict(self):
        return {
            'name': self.channel.name,
            'uuid': self.channel.uuid,
        }

    def __str__(self):
        return self.name