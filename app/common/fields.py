import uuid
import base64
import posixpath
from datetime import datetime

from django.core.files.base import ContentFile
from django.core.files.utils import validate_file_name
from django.db import models

from rest_framework.fields import SkipField
from rest_framework import serializers


def _generate_filename(inst_upload_to, filename) -> str:
    ext = filename.split('.')[-1]
    hash_name = str(uuid.uuid4())
    filename = f"{hash_name}.{ext}"
    upload_to = f"{inst_upload_to}/%Y/%m/%d/"
    dirname = datetime.now().strftime(upload_to)
    filename = posixpath.join(dirname, filename)
    filename = validate_file_name(filename, allow_relative_path=True)
    return filename


class FileField(models.FileField):
    def generate_filename(self, instance, filename):
        return self.storage.generate_filename(_generate_filename(self.upload_to, filename))


class ImageField(models.ImageField):
    def generate_filename(self, instance, filename):
        return self.storage.generate_filename(_generate_filename(self.upload_to, filename))


class Base64FieldMixin:
    def _decode(self, data):
        if isinstance(data, str) and data.startswith('data:'):
            # base64 encoded file - decode
            format, datastr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension
            if ext[:3] == 'svg':
                ext = 'svg'

            data = ContentFile(base64.b64decode(datastr), name=f"{uuid.uuid4()}.{ext}")

        elif isinstance(data, str) and data.startswith('http'):
            raise SkipField()

        return data

    def to_internal_value(self, data):
        data = self._decode(data)
        return super().to_internal_value(data)


class Base64ImageField(Base64FieldMixin, serializers.ImageField):
    pass


class Base64FileField(Base64FieldMixin, serializers.FileField):
    pass
