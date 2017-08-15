from django.conf.urls import url

from . import views

app_name = 'wiki'
urlpatterns = [
    url(r'^$', views.WikiIndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-_\w]+)$', views.PageDetailView.as_view(), name='page')
]
