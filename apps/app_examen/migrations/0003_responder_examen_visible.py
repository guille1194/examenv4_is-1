# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0002_responder_examen'),
    ]

    operations = [
        migrations.AddField(
            model_name='responder_examen',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
