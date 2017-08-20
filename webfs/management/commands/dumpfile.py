import os
import zipfile
from django.core.management.base import BaseCommand
from webfs.models import WebFile


class DirDumper(object):

    def __init__(self, path):
        self.path = os.path.abspath(path)

    def __call__(self, path, file):
        with open(os.path.join(self.path, path), 'wb') as f:
            f.write(file.read())

    def __enter__(self):
        if os.path.exists(self.path):
            if os.path.isdir(self.path):
                pass
            else:
                raise RuntimeError('There is a file at the path')
        else:
            os.makedirs(self.path)

    def __exit__(self, *args, **kwargs):
        pass


class ZipDumper(object):

    def __init__(self, path):
        self.path = path
        self._zip_file = None

    def __call__(self, path, file):
        with self._zipfile.open(path, 'w') as f:
            f.write(file.read())

    def __enter__(self):
        self._zipfile = zipfile.ZipFile(self.path, 'w')

    def __exit__(self, *args, **kwargs):
        self._zipfile.close()


class Command(BaseCommand):
    help = 'Dump web files from storage to local'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        path = os.path.expanduser(options['path'])
        if path.endswith('.zip'):
            dumper = ZipDumper(path)
        else:
            dumper = DirDumper(path)

        with dumper:
            for wf in WebFile.objects.all():
                dumper(wf.file.name, wf.file)
                self.stdout.write('Dump: %s' % wf.file)
        self.stdout.write('Done.')
