from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from apps.main.models import PrivateDocument, PublicDocument


def private_document_view(request, pk):
    obj = get_object_or_404(PrivateDocument, pk=pk)
    return HttpResponse(obj.file.url)


def public_document_view(request, pk):
    obj = get_object_or_404(PublicDocument, pk=pk)
    return HttpResponse(obj.file.url)
