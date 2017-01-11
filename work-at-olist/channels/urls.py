from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from channels import views


urlpatterns = [
    url(r'^api/v1/channels/$', views.ChannelListAPIView.as_view()),
    url(r'^api/v1/channels/(?P<uuid>[\w-]+)/$', views.ChannelDetailAPIView.as_view()),
    url(r'^api/v1/category/(?P<uuid>[\w-]+)/$', views.ChannelCategoryDetailAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)