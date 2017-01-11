from rest_framework import generics, mixins
from rest_framework.response import Response

from .models import Channel, ChannelCategory
from .serializers import ChannelSerializer, ChannelDetailSerializer, ChannelCategorySerializer


class BaseAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ChannelListAPIView(BaseAPIView):
    serializer_class = ChannelSerializer

    def get_queryset(self):
        return Channel.objects.filter(is_active=True)


class ChannelDetailAPIView(ChannelListAPIView):
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