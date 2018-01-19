from django.db import models
import datetime


class CommonFields(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    description = models.CharField(max_length=300)
    # TODO add user field to common model

    class Meta:
        abstract = True


class Packages(models.Model, CommonFields):
    name = models.CharField(max_length=31)
    description = models.CharField(max_length=150)
    consist_of_files = models.ManyToManyField(Files)


class Files(models.Model, CommonFields):
    initial_filename = models.CharField(max_length=120)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=PROTECT)
    file = models.FileField()


class Manufacturer(models.Model, CommonFields):
    full_name = models.CharField(max_length=120)
    short_name = models.CharField(max_length=10)

