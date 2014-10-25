# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comment_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='code',
            field=models.CharField(max_length=15),
        ),
    ]
