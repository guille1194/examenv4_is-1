# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0006_auto_20161205_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realizar_examen',
            name='id_pregunta',
        ),
    ]
