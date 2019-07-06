from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^weather/',include('weather.urls')),
    url(r'^$', include('weather.urls')),

]
