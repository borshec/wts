# Generated by Django 2.0.1 on 2018-02-03 13:14

from django.db import migrations, models
import veiledfiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('veiledfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='veiledfile',
            name='file',
            field=veiledfiles.models.VeiledFileField(upload_to=veiledfiles.models.VeiledFile.change_filename),
        ),
    ]
