from django.views import generic
from .models import Post


class PostListView(generic.ListView):

    template_name = 'blog/index.html'

    def get_queryset(self):
        q = Post.objects.filter(status=Post.STATUS_PUBLISHED)
        return q.order_by('-created_at')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
