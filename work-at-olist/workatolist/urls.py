from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Work AT Olist API')
# schema_view = get_schema_view(title='Work AT Olist API')


urlpatterns = [
    url(r'^', include('channels.urls')),
    url(r'^$', schema_view),
]
