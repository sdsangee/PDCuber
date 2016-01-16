# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdblogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_date', '-published_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to='', blank=True),
        ),
    ]
