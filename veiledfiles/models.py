from django.db import models
from django.db.models.fields.files import FileField, FieldFile, File
from uuid import uuid4
from hashlib import sha1
from django.conf import settings
import pdb


class VeiledFieldFile(FieldFile):

    def url(self):
        link = super().url
        link = link.replace(settings.MEDIA_URL, settings.MEDIA_RAW_URL, 1)
    #    pdb.set_trace()
        return link

    def __str__(self):
        try:
            return self.initial_filename
        except:
            return self.name
        return


class VeiledFileField(FileField):
    attr_class = VeiledFieldFile


class VeiledFile(models.Model):

    def change_filename(self, filename):
        return str(uuid4())

    initial_filename = models.CharField(max_length=120, editable=False)
    file = VeiledFileField(upload_to=change_filename)
    sha1_digest = models.BinaryField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.initial_filename = self.file.name
        f = File(self.file)
        hasher = sha1()
        for chunk in f.chunks():
            hasher.update(chunk)
        self.sha1_digest = hasher.digest()
        super().save(*args, **kwargs)

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        instance.file.initial_filename = values[field_names.index('initial_filename')]
        return instance

    #def get_file_

    def __str__(self):
        return "{} ( {} )".format(self.id, self.initial_filename)

class TestModel(models.Model):
    File = FileField()