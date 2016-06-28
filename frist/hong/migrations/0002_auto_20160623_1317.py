# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hong', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costomer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=50)),
                ('robot_page', models.CharField(max_length=250)),
                ('robot_key', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('contact_title', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=15)),
                ('fax', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=10)),
                ('website', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(verbose_name=b'date published')),
                ('update_time', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
