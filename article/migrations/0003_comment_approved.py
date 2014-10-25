# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20141025_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=b'False'),
            preserve_default=True,
        ),
    ]
