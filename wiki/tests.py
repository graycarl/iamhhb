from django.test import TestCase
from django.urls import reverse
from .models import Page


# Create your tests here.
class PostModelTest(TestCase):

    def test_render_markdown(self):
        p = Page(content='aa')
        self.assertEqual(p.content_html, '<p>aa</p>\n')
        p = Page(content='[[aa|bb]]')
        self.assertTrue('href="bb"' in p.content_html)


class PostViewTest(TestCase):

    def test_post_view(self):
        p = Page(
            slug='first-blog',
            title='First blog',
            content='I am hhb',
        )
        p.save()
        url = reverse('wiki:page', args=(p.slug,))
        resp = self.client.get(url)
        self.assertContains(resp, 'I am hhb')
