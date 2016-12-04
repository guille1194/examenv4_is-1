# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_examen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='responder_examen',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('id_alumno', models.ForeignKey(to='app_examen.alumno')),
                ('id_examen', models.ForeignKey(to='app_examen.examen')),
            ],
        ),
    ]
