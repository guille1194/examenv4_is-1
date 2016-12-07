# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0012_realizar_examen_id_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='terminar',
            field=models.BooleanField(default=False),
        ),
    ]
