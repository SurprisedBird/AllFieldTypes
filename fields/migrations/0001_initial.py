# Generated by Django 2.2.6 on 2019-10-31 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllFieldsTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('big_int', models.BigIntegerField()),
                ('binary', models.BinaryField()),
                ('boolean', models.BooleanField()),
                ('char', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('date_time', models.DateTimeField()),
                ('decimal', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('duration', models.DurationField(default=datetime.timedelta(days=270))),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('file', models.FileField(default=None, null=True, upload_to='')),
                ('path_field', models.FilePathField(null=True, path=None)),
                ('float_field', models.FloatField(default=3.0)),
                ('image', models.ImageField(max_length=40, null=True, upload_to=None)),
            ],
        ),
    ]
