# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0013_auto_20151101_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapsData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance_float', models.FloatField(verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe \xd1\x83\xd1\x81\xd1\x82\xd1\x8c\xd1\x8f \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8')),
                ('map_1', models.DecimalField(null=True, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xbe\xd1\x8f\xd1\x82\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9 25 %\xd0\x92\xd0\x9f (\xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd \xd1\x80\xd0\xb0\xd0\xb7 \xd0\xb2 4 \xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0)', max_digits=5, decimal_places=2, blank=True)),
                ('map_2', models.DecimalField(null=True, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9 10% \xd0\x92\xd0\x9f (\xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd \xd1\x80\xd0\xb0\xd0\xb7 \xd0\xb2 10 \xd0\xbb\xd0\xb5\xd1\x82)', max_digits=5, decimal_places=2, blank=True)),
                ('map_3', models.DecimalField(null=True, verbose_name=b'\xd0\x92\xd1\x8b\xd1\x81\xd0\xbe\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9 5% \xd0\x92\xd0\x9f (\xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd \xd1\x80\xd0\xb0\xd0\xb7 \xd0\xb2 20 \xd0\xbb\xd0\xb5\xd1\x82)', max_digits=5, decimal_places=2, blank=True)),
                ('map_4', models.DecimalField(null=True, verbose_name=b'\xd0\x9d\xd0\xb8\xd0\xb7\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xbe\xd1\x8f\xd1\x82\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9 1% \xd0\x92\xd0\x9f (\xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd \xd1\x80\xd0\xb0\xd0\xb7 \xd0\xb2 100 \xd0\xbb\xd0\xb5\xd1\x82)', max_digits=5, decimal_places=2, blank=True)),
                ('map_5', models.DecimalField(null=True, verbose_name=b'\xd0\x9d\xd0\xb8\xd0\xb7\xd0\xba\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9 0.5% \xd0\x92\xd0\x9f (\xd0\xbe\xd0\xb4\xd0\xb8\xd0\xbd \xd1\x80\xd0\xb0\xd0\xb7 \xd0\xb2 200 \xd0\xbb\xd0\xb5\xd1\x82)', max_digits=5, decimal_places=2, blank=True)),
                ('map_6', models.DecimalField(null=True, verbose_name=b'\xd0\x9d\xd0\xb5\xd1\x82 \xd1\x81\xd1\x83\xd1\x89\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb7\xd0\xb0\xd1\x82\xd0\xbe\xd0\xbf\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', max_digits=5, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'MapsData',
                'managed': True,
            },
        ),
    ]
