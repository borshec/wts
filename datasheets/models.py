from django.db import models
import datetime


class CommonFields(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    description = models.CharField(max_length=300)
    # TODO: add user field to common model

    class Meta:
        abstract = True


class Manufacturer(CommonFields):
    full_name = models.CharField(max_length=120)
    short_name = models.CharField(max_length=10)


class Datasheet(CommonFields):
    initial_filename = models.CharField(max_length=120)
    file = models.FileField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    # TODO: Add uuid field with uniqueness

class DatasheetsPackage(CommonFields):
    name = models.CharField(max_length=31)
    consist_of_files = models.ManyToManyField(Datasheet)




