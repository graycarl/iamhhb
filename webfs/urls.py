from django.conf.urls import url

from . import views

app_name = 'webfs'
urlpatterns = [
    url(r'^(?P<id>\d+)$', views.file_view, name='file_by_id'),
    url(r'^(?P<name>[-_.\w]+)$', views.file_view, name='file_by_name')
]
