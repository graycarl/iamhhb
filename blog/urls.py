from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='index'),
    url(r'^(?P<slug>[-_\w]+)$', views.PostDetailView.as_view(), name='post')
]
