from django.contrib import admin
from django.urls import path

from django_project.views import (
    public_document_view,
    private_document_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('private-doc/<int:pk>/', private_document_view),
    path('public-doc/<int:pk>/', public_document_view),
]
