# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0004_auto_20161204_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizar_examen',
            name='puntuacion',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
