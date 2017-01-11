from rest_framework import generics, mixins

from .models import Channel
from .serializers import ChannelSerializer


class BaseAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ChannelListAPIView(BaseAPIView):
    queryset = Channel.objects.filter(is_active=True)
    serializer_class = ChannelSerializer
