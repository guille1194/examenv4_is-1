# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0005_auto_20161205_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='realizar_examen',
            name='id_pregunta',
            field=models.ForeignKey(blank=True, to='app_examen.pregunta', null=True),
        ),
        migrations.AddField(
            model_name='realizar_examen',
            name='id_pregunta_respuesta',
            field=models.ManyToManyField(to='app_examen.pregunta_respuesta', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='realizar_examen',
            name='id_respuesta',
            field=models.ForeignKey(blank=True, to='app_examen.respuesta', null=True),
        ),
    ]
