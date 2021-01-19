from django.conf.urls import url
from .views import *
from django.urls import path,include




urlpatterns = [
    url(r'^$',FlavorListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$',FlavorDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$',FlavorUpdateView.as_view(), name='update'),
    url(r'^create/$',FlavorCreateView.as_view(), name='create'),
    url(r'^api/$',FlavorCreateReadView.as_view(), name='flavor_rest_api'),
    url(r'^api/(?P<pk>\d+)/$',FlavorReadUpdateDeleteView.as_view(), name='flavor_rest_api'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] 