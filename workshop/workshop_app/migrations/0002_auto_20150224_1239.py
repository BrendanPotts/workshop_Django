# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='lable',
            field=models.CharField(max_length=200, verbose_name=b'lable'),
            preserve_default=True,
        ),
    ]
