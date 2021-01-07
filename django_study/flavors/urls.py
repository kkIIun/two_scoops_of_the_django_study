from django.conf.urls import url
from .views import *



urlpatterns = [
    url(r'^$',FlavorListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$',FlavorDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$',FlavorUpdateView.as_view(), name='update'),
    url(r'^create/$',FlavorCreateView.as_view(), name='create'),
] 