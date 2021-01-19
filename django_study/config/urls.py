from django.contrib import admin
from django.urls import path,include
from flavors.views import *
import flavors.urls
import account.urls
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^flavor/', include(flavors.urls)),
    url(r'^sign/', include(account.urls)),
]
