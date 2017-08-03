import json
import uuid
import mimetypes
from django.db import models
from django.utils import timezone


class JsonField(models.Field):

    description = u"Convert base type value to json string"

    def __init__(self, use_db_null=False, *args, **kwargs):
        """
        :use_db_null:
            if true, we set database column to NULL when value is None,
            else, we set database column to string 'null' when value is None
        """
        self.use_db_null = use_db_null
        super(JsonField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(JsonField, self).deconstruct()
        kwargs['use_db_null'] = self.use_db_null
        return name, path, args, kwargs

    def get_internal_type(self):
        return 'CharField'

    def from_db_value(self, value, expression, connection, context):
        if not value:
            return None
        return json.loads(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None and self.use_db_null:
            return None
        data = json.dumps(value)
        if self.max_length is not None and len(data) > self.max_length:
            raise RuntimeError('Data is too long for the database column.')
        return data


def upload_to(ins, fn):
    prefix = timezone.now().strftime('%y-%m-%d')
    mm, encoding = mimetypes.guess_type(fn)
    if encoding is not None:
        raise NotImplementedError('We currently do not support encoding.')
    if mm is None:
        raise RuntimeError('Unknown mimetype for filename: ' + fn)
    exts = mimetypes.guess_all_extensions(mm)
    if '.jpeg' in exts:
        ext = '.jpeg'
    elif '.txt' in exts:
        ext = '.txt'
    else:
        ext = exts[0]
    return '{}-{}{}'.format(prefix, uuid.uuid4().hex[:8], ext)


class WebFile(models.Model):
    file = models.FileField(upload_to=upload_to)
    mimetype = models.CharField(max_length=32)
    size = models.PositiveIntegerField()
    metadata = JsonField(use_db_null=True, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        self.mimetype, _ = mimetypes.guess_type(self.file.name)
        self.size = self.file.size
