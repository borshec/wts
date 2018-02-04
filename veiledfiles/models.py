from django.db import models
from django.db.models.fields.files import FileField, FieldFile, File
from uuid import uuid4
from hashlib import sha1, blake2b
from django.conf import settings
from mimetypes import guess_type
import pdb


class VeiledFieldFile(FieldFile):

    def url(self):
        return str.replace(super().url, settings.MEDIA_URL, settings.MEDIA_RAW_URL, 1)

    def __str__(self):
        try:
            return self.initial_filename
        except:
            return self.name
        return


class VeiledFileField(FileField):
    attr_class = VeiledFieldFile


class VeiledFile(models.Model):
    # TODO: Check uniquenes of hexdigest

    blake2b_digest_size = 16

    def change_filename(self, filename):
        return str(uuid4())

    initial_filename = models.CharField(max_length=120, editable=False)
    file = VeiledFileField(upload_to=change_filename)
    hexdigest = models.CharField(max_length=blake2b_digest_size*2, unique=True, editable=False)
    mime_type = models.CharField(max_length=127, editable=False)

    def save(self, *args, **kwargs):
        self.initial_filename = self.file.name
        self.mime_type = guess_type(self.initial_filename)[0]
        f = File(self.file)
        hasher = blake2b(digest_size=self.blake2b_digest_size)
        for chunk in f.chunks():
            hasher.update(chunk)
        self.hexdigest = hasher.hexdigest()
        super().save(*args, **kwargs)

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        instance.file.initial_filename = values[field_names.index('initial_filename')]
        return instance

    def __str__(self):
        return "{} ( {} )".format(self.id, self.initial_filename)

class TestModel(models.Model):
    File = FileField()