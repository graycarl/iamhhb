from django.shortcuts import get_object_or_404
from django.http import FileResponse
from .models import WebFile


def file_view(request, id=None, name=None):
    if id is not None:
        wf = get_object_or_404(WebFile, id=id)
    elif name is not None:
        wf = get_object_or_404(WebFile, file=name)
    else:
        raise RuntimeError('Need id or name')
    resp = FileResponse(wf.file, content_type=wf.mimetype)
    return resp
