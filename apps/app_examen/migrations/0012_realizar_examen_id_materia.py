# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0011_remove_realizar_examen_id_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='realizar_examen',
            name='id_materia',
            field=models.ForeignKey(blank=True, to='app_examen.materia', null=True),
        ),
    ]
