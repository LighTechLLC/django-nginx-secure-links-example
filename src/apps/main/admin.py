from django.contrib import admin

from apps.main.models import PublicDocument, PrivateDocument

admin.site.register(PublicDocument)
admin.site.register(PrivateDocument)
