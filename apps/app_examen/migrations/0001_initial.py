# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='alumno',
            fields=[
                ('n_control', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('correo', models.EmailField(max_length=254)),
                ('categoria', models.CharField(default=b'estudiante', max_length=64)),
                ('user_perfil', models.OneToOneField(related_name='alumno', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='alumno_materia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('alum', models.ForeignKey(related_name='alumno', to='app_examen.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='examen',
            fields=[
                ('id_examen', models.AutoField(serialize=False, primary_key=True)),
                ('unidad', models.IntegerField()),
                ('id_alumno', models.ForeignKey(blank=True, to='app_examen.alumno', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='maestro',
            fields=[
                ('n_empleado', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('correo', models.EmailField(max_length=254)),
                ('categoria', models.CharField(default=b'maestros', max_length=64, null=True)),
                ('user_perfil', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='materia',
            fields=[
                ('serie', models.SlugField(max_length=64, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('maestro_a', models.ForeignKey(related_name='maestro_inparte', to='app_examen.maestro', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('semestre', models.IntegerField()),
                ('dificultad', models.CharField(max_length=64, choices=[(b'Facil', b'Facil'), (b'Intermedio', b'Intermedio'), (b'Dificil', b'Dificil')])),
                ('valor', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('materia', models.ForeignKey(related_name='mat', to='app_examen.materia')),
            ],
        ),
        migrations.CreateModel(
            name='pregunta_respuesta',
            fields=[
                ('id_pregunta_respuesta', models.AutoField(serialize=False, primary_key=True)),
                ('id_pregunta', models.ForeignKey(to='app_examen.pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='respuesta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=64)),
                ('correcta', models.BooleanField()),
                ('pregun', models.ForeignKey(related_name='pregunt', to='app_examen.pregunta')),
            ],
        ),
        migrations.AddField(
            model_name='pregunta_respuesta',
            name='id_respuesta',
            field=models.ManyToManyField(to='app_examen.respuesta'),
        ),
        migrations.AddField(
            model_name='examen',
            name='id_materia',
            field=models.ForeignKey(related_name='idmate', to='app_examen.materia'),
        ),
        migrations.AddField(
            model_name='examen',
            name='id_pregunta_respuesta',
            field=models.ManyToManyField(to='app_examen.pregunta_respuesta'),
        ),
        migrations.AddField(
            model_name='alumno_materia',
            name='materi',
            field=models.ForeignKey(related_name='materia', to='app_examen.materia'),
        ),
        migrations.AlterUniqueTogether(
            name='examen',
            unique_together=set([('id_materia', 'unidad')]),
        ),
        migrations.AlterUniqueTogether(
            name='alumno_materia',
            unique_together=set([('alum', 'materi')]),
        ),
    ]
