from urllib.parse import urljoin
from django.db import connection, transaction
from django.conf import settings
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.utils.deconstruct import deconstructible

from .models import PGFile


@deconstructible
class PostgreStorage(Storage):
    """使用 PostgreSQL 的 LargeObject 特性来存储文件"""

    def __init__(self):
        self.base_url = settings.MEDIA_URL

    def lobject(self, *args, **kwargs):
        assert connection.vendor == 'postgresql'
        connection.ensure_connection()
        return connection.connection.lobject(*args, **kwargs)

    @transaction.atomic
    def _open(self, name, mode='rb'):
        pgfile = PGFile.objects.get(name=name)
        lo = self.lobject(pgfile.oid, mode)
        return ContentFile(lo.read())

    @transaction.atomic
    def _save(self, name, content):
        pgfile = PGFile(name=name, size=content.size)
        lo = self.lobject(0, mode='wb')
        for chunk in content.chunks():
            lo.write(chunk)
        lo.close()
        pgfile.oid = lo.oid
        pgfile.save()
        return name

    @transaction.atomic
    def delete(self, name):
        pgfile = PGFile.objects.get(name=name)
        lo = self.lobject(pgfile.oid)
        lo.unlink()
        pgfile.delete()

    def exists(self, name):
        return PGFile.objects.filter(name=name).exists()

    def size(self, name):
        pgfile = PGFile.objects.get(name=name)
        return pgfile.size

    def url(self, name):
        if self.base_url is None:
            raise ValueError("This file is not accessible via a URL.")
        return urljoin(self.base_url, name)
