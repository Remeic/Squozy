from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.create_shorturl, name='create_shorturl'),
    url(r'^(?P<code>[%&+ \w]+)/$',views.url_redirection,name='url_redirection'),
    url(r'^api/get/(?P<code>[%&+ \w]+)/$',views.api_url_response,name='api_url_response'),
    url(r'^api/request/$',views.api_url_request,name='api_url_request'),
 ]

