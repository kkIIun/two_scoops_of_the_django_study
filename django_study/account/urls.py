from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^in/$',sign_in_function, name='sign_in'),
    url(r'^up/$',sign_up_function, name='sign_up'),
    url(r'^out/$',sing_out_function, name='sign_out'),
] 