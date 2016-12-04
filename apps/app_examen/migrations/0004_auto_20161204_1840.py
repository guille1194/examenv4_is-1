# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0003_responder_examen_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='realizar_examen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('puntuacion', models.IntegerField()),
                ('id_alumno', models.ForeignKey(to='app_examen.alumno')),
                ('id_examen', models.ForeignKey(to='app_examen.examen')),
            ],
        ),
        migrations.RemoveField(
            model_name='responder_examen',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='responder_examen',
            name='id_examen',
        ),
        migrations.DeleteModel(
            name='responder_examen',
        ),
    ]
