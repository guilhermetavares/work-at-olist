import requests
import re

from django.utils.text import slugify
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from channels.models import Channel, ChannelCategory


def get_csv_data(csv_file):
    try:
        URLValidator()(csv_file)
        return requests.get(csv_file).text
    except ValidationError:
        try:
            return open(csv_file, 'rb').read().decode()
        except FileNotFoundError:
            return None


def make_channel_data(channel, csv_file):
    data = get_csv_data(csv_file)
    cache_categories = {}
    if data:
        channel, created = Channel.objects.get_or_create(name=channel)
        channel.categories.all().delete()
        for line in re.split("\n", data)[1:-1]:
            parent = None
            print('*' * 100)
            for category in re.split("/", line):
                print(category)
                category = category.strip()
                slug_category = slugify(category)
                
                cache_key = '{0}_{1}'.format(parent.slug if parent else '', slug_category)

                if cache_categories.get(cache_key):
                    parent = cache_categories.get(cache_key)
                    continue
                
                category = channel.categories.create(**{
                    'parent': parent,
                    'name': category,
                    'slug': slug_category,
                })
                print('CREATE', category, category.parent)
                parent = category
                cache_categories.update({cache_key: category})
        ChannelCategory.objects.rebuild()
        return {'status': True, 'message': u'Channel {0} importing successfully, total {1} categories found.'.format(channel, channel.categories.count())}
    return {'status': False, 'message': 'File not found'}
