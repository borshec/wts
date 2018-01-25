from django.db import models
import datetime
import hashlib
from django.core.files import File
from uuid import uuid4


def random_byte_value():
    return str(uuid4()).encode()


def rename_file__assign_fields(instance, filename):
    instance.initial_filename = filename
    f = File(instance.dsfile)
    hasher = hashlib.sha1()
    for chunk in f.chunks():
        hasher.update(chunk)
    instance.sha1_digest = hasher.digest()
    return str(uuid4())


class CommonFields(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now,
                                         editable=False)
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
    dsfile = models.FileField(upload_to=rename_file__assign_fields)
    initial_filename = models.CharField(max_length=120, editable=False)
    sha1_digest = models.BinaryField(unique=True, editable=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ( {} )".format(self.id, self.initial_filename)

    # TODO: change link on file in admin panel
    # TODO: move renaming function to class


class Package(CommonFields):
    name = models.CharField(max_length=31)
    datasheets = models.ManyToManyField(Datasheet)
