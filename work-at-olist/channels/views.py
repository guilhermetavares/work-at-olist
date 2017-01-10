from rest_framework import generics

from .models import Channel
from .serializers import ChannelSerializer


class ChannelListAPIView(generics.ListCreateAPIView):
	queryset = Channel.objects.filter(is_active=True)
	serializer_class = ChannelSerializer