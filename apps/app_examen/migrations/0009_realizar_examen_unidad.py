# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0008_auto_20161205_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='realizar_examen',
            name='unidad',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
