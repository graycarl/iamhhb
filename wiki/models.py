import mistune
from django.db import models
from django.utils import timezone
from .libs.markdown import Renderer


class Page(models.Model):

    markdown = mistune.Markdown(renderer=Renderer())

    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField('Tag')

    visit_count = models.PositiveIntegerField(default=0)
    visit_last_at = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def _render_content(self):
        self.markdown.renderer.reset_toc()
        self._content_html = self.markdown(self.content)
        self._content_toc = self.markdown.renderer.render_toc()

    @property
    def content_html(self):
        if not hasattr(self, '_content_html'):
            self._render_content()
        return self._content_html

    @property
    def content_toc(self):
        if not hasattr(self, '_content_toc'):
            self._render_content()
        return self._content_toc

    def record_visit(self):
        self.visit_count += 1
        self.visit_last_at = timezone.now()


class Tag(models.Model):

    slug = models.SlugField(max_length=100, unique=True)
    text = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def page_count(self):
        return self.page_set.count()
