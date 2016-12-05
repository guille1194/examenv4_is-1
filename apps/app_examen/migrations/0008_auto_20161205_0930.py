# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0007_remove_realizar_examen_id_pregunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realizar_examen',
            name='id_examen',
            field=models.ForeignKey(blank=True, to='app_examen.examen', null=True),
        ),
        migrations.RemoveField(
            model_name='realizar_examen',
            name='id_respuesta',
        ),
        migrations.AddField(
            model_name='realizar_examen',
            name='id_respuesta',
            field=models.ManyToManyField(to='app_examen.respuesta', null=True, blank=True),
        ),
    ]
