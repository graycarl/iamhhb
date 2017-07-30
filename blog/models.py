import mistune
from django.db import models
from .libs.markdown import Renderer


class Post(models.Model):
    """博客 Model"""

    markdown = mistune.Markdown(renderer=Renderer())

    slug = models.SlugField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    summary = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.slug

    @property
    def html_content(self):
        return self.markdown(self.content)
