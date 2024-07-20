from django.db import models


class PrivateDocument(models.Model):
    file = models.FileField(upload_to='private/documents')


class PublicDocument(models.Model):
    file = models.FileField(upload_to='documents')
