from django.http import Http404

from rest_framework import generics, mixins
from rest_framework.response import Response

from rest_framework_swagger import renderers

from .models import Channel, ChannelCategory
from .serializers import ChannelSerializer, ChannelDetailSerializer, ChannelCategorySerializer


class BaseAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ChannelListAPIView(BaseAPIView):
    """
    Returns a list of all **active** accounts in the system.

    For more details on how accounts are activated please [see here][ref].

    [ref]: https://tavares-work-at-olist.herokuapp.com/api/v1/channels/?format=json
    """

    serializer_class = ChannelSerializer

    def get_queryset(self):
        return Channel.objects.filter(is_active=True)


class ChannelDetailAPIView(ChannelListAPIView):
    """
    Returns a fully detail of **channel**
    Showing its category tree, [see here][ref]
    [ref]: https://tavares-work-at-olist.herokuapp.com/api/v1/channels/bfeaf7e1-4606-4887-8e10-235e4156b270/?format=json
    """
    serializer_class = ChannelDetailSerializer

    def get_object(self, uuid):
        try:
            return self.get_queryset().get(uuid=uuid)
        except Channel.DoesNotExist:
            raise Http404


    def get(self, request, uuid, format=None):
        snippet = self.get_object(uuid)
        serializer = ChannelDetailSerializer(snippet)
        return Response(serializer.data)


class ChannelCategoryDetailAPIView(BaseAPIView):
    '''
    Returns a fully detail of a **category**
    Showing its category tree, [see here][ref]
    [ref]: https://tavares-work-at-olist.herokuapp.com/api/v1/category/b407430e-6315-4f02-a14f-affd7f9ad81b/?format=json
    '''
    serializer_class = ChannelCategorySerializer

    def get_queryset(self):
        return ChannelCategory.objects.all()

    def get_object(self, uuid):
        try:
            return self.get_queryset().get(uuid=uuid)
        except Channel.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):
        snippet = self.get_object(uuid)
        serializer = self.serializer_class(snippet)
        return Response(serializer.data)