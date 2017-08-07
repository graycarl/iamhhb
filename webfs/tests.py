from django.test import TestCase
from django.urls import reverse
from django.core.files.base import ContentFile
from .models import WebFile


class WebFileModelTest(TestCase):

    def test_clean(self):
        file = ContentFile(b'b'*1024)
        file.name = 'abc.jpg'
        file.size = 1024
        wf = WebFile(file=file)
        wf.full_clean()
        wf.save()
        self.assertEqual(wf.mimetype, 'image/jpeg')
        self.assertEqual(wf.size, 1024)


class WebFileViewTest(TestCase):

    def test_view(self):
        file = ContentFile(b'b'*1024)
        file.name = 'abc.jpg'
        file.size = 1024
        wf = WebFile(file=file)
        wf.full_clean()
        wf.save()
        urls = [reverse('webfs:file_by_id', args=(wf.id,)),
                reverse('webfs:file_by_name', args=(wf.file,))]
        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response['Content-Type'], 'image/jpeg')
            self.assertTrue(response.streaming)
            self.assertEqual(next(response.streaming_content)[:4], b'bbbb')
