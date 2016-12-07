# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0013_respuesta_terminar'),
    ]

    operations = [
        migrations.AddField(
            model_name='realizar_examen',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
