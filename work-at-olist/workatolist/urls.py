from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from channels.views import ChannelListAPIView

# router = routers.DefaultRouter()
# router.register(r'channel', ChannelListAPIView)
# # router.register(r'category', CategoryView)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('channels.urls')),
]
