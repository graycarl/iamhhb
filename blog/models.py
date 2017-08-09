import mistune
from django.db import models
from .libs.markdown import Renderer


class Post(models.Model):
    """博客 Model"""

    STATUS_PUBLISHED = 'published'
    STATUS_DRAFT = 'draft'
    STATUS_DELETED = 'deleted'
    STATUSES = [
        (STATUS_DRAFT, u'草稿'),
        (STATUS_PUBLISHED, u'已发布'),
        (STATUS_DELETED, u'已删除')
    ]

    markdown = mistune.Markdown(renderer=Renderer())

    slug = models.SlugField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    summary = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    status = models.CharField(max_length=20, choices=STATUSES)

    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

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
