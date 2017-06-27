from django.db import models


class Post(models.Model):
    """博客 Model
    """

    slug = models.SlugField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)

    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return self.slug
