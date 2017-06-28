from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostModelTest(TestCase):

    def test_render_markdown(self):
        p = Post(content='aa')
        self.assertEqual(p.html_content, '<p>aa</p>\n')


class PostViewTest(TestCase):

    def test_post_view(self):
        p = Post(
            slug='first-blog',
            title='First blog',
            content='I am hhb',
        )
        p.save()
        url = reverse('post', args=(p.slug,))
        resp = self.client.get(url)
        self.assertContains(resp, 'I am hhb')
