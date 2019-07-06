from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'weather'

urlpatterns = [
    url(r'^getdata/', views.index),
    # defining the view for root URL
    url(r'^$', views.index, name='index'),
    url(r'^mars/',views.mars, name='mars'),
    url(r'^earth/', views.earth, name='earth'),
    url(r'^references/', views.references, name='references'),

]
