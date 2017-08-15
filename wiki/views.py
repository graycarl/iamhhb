from django.views import generic
from .models import Page


class WikiIndexView(generic.ListView):

    template_name = 'wiki/index.html'

    def get_queryset(self):
        q = Page.objects.filter()
        return q.order_by('-created_at')

    # def get(self, request):
    #     return render(request, 'wiki/index.html')


class PageDetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/page.html'

    def get_object(self, *args, **kwargs):
        obj = super(PageDetailView, self).get_object(*args, **kwargs)
        obj.record_visit()
        obj.save()
        return obj
