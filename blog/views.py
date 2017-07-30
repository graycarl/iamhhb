from django.views import generic
from .models import Post


class PostListView(generic.ListView):

    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
