from django.db import models
import datetime, hashlib, random
from django.core.files import File
from uuid import uuid4


def random_byte_value():
    return str(uuid4()).encode()

def file_hash(file):
    f = File(file)
    hash_obj = hashlib.sha1()
    for chunk in f.chunks():
        hash_obj.update(chunk)
    return hash_obj.digest()

def rename_file(file):


class CommonFields(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now, editable=False)
    description = models.CharField(max_length=300)
    # TODO: add user field to common model

    class Meta:
        abstract = True


class Manufacturer(CommonFields):
    full_name = models.CharField(max_length=120)
    short_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return "{} ({}, {})".format(self.id, self.short_name, self.full_name)


class Datasheet(CommonFields):
    initial_filename = models.CharField(max_length=120, editable=False)
    file = models.FileField()
    sha1_digest = models.BinaryField(unique=True, editable=False, default=random_byte_value)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ( {} )".format(self.id, self.file)

    def save(self, *args, **kwargs):
        self.sha1_digest=file_hash(self.file)
        self.initial_filename = str(self.file)
        print("TEST")
        super().save(*args, **kwargs)

    # TODO: Change filenames on upload
    # TODO: Evaluate md5 on any other hash of file
    # TODO: Hash field must be unique
    # TODO: Add uuid field with uniqueness

class Package(CommonFields):
    name = models.CharField(max_length=31)
    datasheets = models.ManyToManyField(Datasheet)




