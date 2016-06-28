# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hong', '0002_auto_20160623_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costomer',
            name='create_time',
            field=models.DateTimeField(verbose_name=b'date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='costomer',
            name='update_time',
            field=models.DateTimeField(verbose_name=b'date'),
            preserve_default=True,
        ),
    ]
