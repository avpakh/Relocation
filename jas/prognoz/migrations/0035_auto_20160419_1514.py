# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0034_auto_20160412_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapsbrovka',
            name='brovka0_50',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\x9e\xd1\x82 0 \xd0\xb4\xd0\xbe 50 \xd1\x81\xd0\xbc \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='mapsbrovka',
            name='brovka200',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\xa1\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5 2 \xd0\xbc \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='mapsbrovka',
            name='brovka50_80',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\x9e\xd1\x82 50 \xd0\xb4\xd0\xbe 80 \xd1\x81\xd0\xbc \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='mapsbrovka',
            name='brovka80_200',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\x9e\xd1\x82 80 \xd0\xb4\xd0\xbe 200 \xd1\x81\xd0\xbc \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='prognozgraph',
            name='discharge',
            field=models.DecimalField(verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x85\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8, \xd0\xba\xd1\x83\xd0\xb1.\xd0\xbc/\xd1\x81', max_digits=12, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='prognozgraph',
            name='dist_km',
            field=models.IntegerField(verbose_name=b' \xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe \xd1\x83\xd1\x81\xd1\x82\xd1\x8c\xd1\x8f, \xd0\xba\xd0\xbc '),
        ),
        migrations.AlterField(
            model_name='prognozgraph',
            name='level',
            field=models.DecimalField(verbose_name=b'\xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8, \xd0\xbc', max_digits=12, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='prognozgraph',
            name='time100',
            field=models.DecimalField(verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbe\xd1\x82 \xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb3\xd0\xbd\xd0\xbe\xd0\xb7\xd0\xb0, \xd1\x87', max_digits=5, decimal_places=2),
        ),
    ]
