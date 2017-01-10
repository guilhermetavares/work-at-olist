import factory

from django.utils.text import slugify

from channels.models import Channel, ChannelCategory


class ChannelFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'name {0}'.format(n))

    class Meta:
        model = Channel


class ChannelCategoryFactory(factory.django.DjangoModelFactory):
    channel = factory.SubFactory(ChannelFactory)

    name = factory.Sequence(lambda n: 'name {0}'.format(n))
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))

    class Meta:
        model = ChannelCategory
