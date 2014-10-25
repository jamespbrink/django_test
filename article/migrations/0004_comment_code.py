# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='code',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]
