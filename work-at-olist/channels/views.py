from rest_framework import generics, mixins
from rest_framework.response import Response

from django.http import Http404

from .models import Channel, ChannelCategory
from .serializers import ChannelSerializer, ChannelDetailSerializer, ChannelCategorySerializer


class BaseAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ChannelListAPIView(BaseAPIView):
    """
    Returns a list of all **active** channels in the system.
    The list is paginate by **20** instances per page.
    For more detail, [see here][ref].
    [ref]: http://example.com/activating-accounts
    """

    serializer_class = ChannelSerializer

    def get_queryset(self):
        return Channel.objects.filter(is_active=True)


class ChannelDetailAPIView(ChannelListAPIView):
    """
    This method show all data from a channel, from your uuid

    * ?format=api: To show all the details of api.

    * ?format=json: for json return
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
    Returns a list of all **active** accounts in the system.

    For more details on how accounts are activated please [see here][ref].

    [ref]: /api/v1/channels/bfeaf7e1-4606-4887-8e10-235e4156b270?format=api
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