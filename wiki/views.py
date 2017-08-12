from django.views import generic, View
from django.shortcuts import render
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
