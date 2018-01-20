from django.db import models
import datetime,


class CommonFields(models.Model):
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    description = models.CharField(max_length=300)
    # TODO: add user field to common model

    class Meta:
        abstract = True


class Manufacturer(CommonFields):
    full_name = models.CharField(max_length=120)
    short_name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return "{} ({})".format(self.short_name, self.full_name)


class Datasheet(CommonFields):
    initial_filename = models.CharField(max_length=120)
    file = models.FileField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.initial_filename =
    # TODO: Change filenames on upload
    # TODO: Evaluate md5 on any other hash of file
    # TODO: Hash field must be unique
    # TODO: Add uuid field with uniqueness

class Package(CommonFields):
    name = models.CharField(max_length=31)
    datasheets = models.ManyToManyField(Datasheet)




