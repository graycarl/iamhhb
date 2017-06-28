from django.test import TestCase
from .models import Post


# Create your tests here.
class PostModelTest(TestCase):

    def test_render_markdown(self):
        p = Post(content='aa')
        self.assertEqual(p.html_content, '<p>aa</p>\n')
