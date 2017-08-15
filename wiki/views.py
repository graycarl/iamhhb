from django.views import generic, View
from django.shortcuts import render
from .models import Page


class WikiIndexView(View):

    def get(self, request):
        page = Page.objects.get(slug='home')
        return render(request, 'wiki/index.html', dict(page=page))


class PageDetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/page.html'

    def get_object(self, *args, **kwargs):
        obj = super(PageDetailView, self).get_object(*args, **kwargs)
        obj.record_visit()
        obj.save()
        return obj
