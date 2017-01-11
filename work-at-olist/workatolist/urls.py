from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from channels.views import ChannelListAPIView

schema_view = get_swagger_view(title='Work AT Olist API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('channels.urls')),

    url(r'^$', schema_view),
]
