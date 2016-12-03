from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator,MaxValueValidator
from django.utils import timezone
from multiselectfield import MultiSelectField
import datetime
# Create your models here.
class maestro(models.Model):
	user_perfil = models.OneToOneField(User, related_name="profile")
	n_empleado = models.CharField(max_length=64,primary_key=True)
	nombre = models.CharField(max_length=64)
	correo = models.EmailField()
	categoria = models.CharField(max_length=64,null = True,default="maestros")

	def __unicode__(self):
		return '%s'%(self.n_empleado)

class materia(models.Model):
	serie = models.SlugField(max_length=64, primary_key=True)#forzar al usuario a capyurarlo de una manera expresion regular
	nombre = models.CharField(max_length=64,blank=False)
	maestro_a = models.ForeignKey(maestro, max_length=64,related_name='maestro_inparte')
	#periodo = models.CharField(max_length=64)
	def __unicode__(self):
		return '%s  %s'%(self.serie,self.nombre)

class alumno(models.Model):
	user_perfil = models.OneToOneField(User, related_name="alumno")
	n_control = models.CharField(max_length=8,primary_key=True)
	nombre = models.CharField(max_length=64)
	apellido = models.CharField(max_length=64)
	correo = models.EmailField()
	categoria = models.CharField(max_length=64,default="estudiante")

	def __unicode__(self):
		return '%s'%(self.n_control)

class alumno_materia(models.Model):
	id = models.AutoField(primary_key=True)
	alum = models.ForeignKey(alumno,related_name='alumno')# numero de control
	materi = models.ForeignKey(materia,related_name='materia')#serie de materia

	def __unicode__(self):
		return '%s'%(self.id)

	class Meta:
		unique_together = ('alum','materi')



class pregunta(models.Model):
	id = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=64)
	materia = models.ForeignKey(materia,related_name="mat")
	semestre = models.IntegerField()
	nivel = (('Facil','Facil'),('Intermedio','Intermedio'),('Dificil','Dificil'))
	dificultad = models.CharField(max_length=64,choices=nivel)
	valor = models.PositiveIntegerField( validators=[MinValueValidator(1),MaxValueValidator(100)])

	def __unicode__(self):
		return '%s'%(self.nombre)

	def __str__(self):
		return '%s'%(self.id)

class respuesta(models.Model):
	id = models.AutoField(primary_key=True)
	pregun = models.ForeignKey(pregunta,related_name="pregunt")
	nombre = models.CharField(max_length=64)
	correcta = models.BooleanField()

	def __unicode__(self):
		return u"%s"%(self.nombre)

	def __str__(self):
		return u'%s'%(self.id)

class pregunta_respuesta(models.Model):
	id_pregunta_respuesta = models.AutoField(primary_key=True)
	id_pregunta = models.ForeignKey(pregunta)
	id_respuesta = models.ManyToManyField(respuesta)

	def __unicode__(self):
		return u'%s'%(self.id_pregunta_respuesta)

	def get_pregunta(self):
		return "\n".join([p.nombre for p in self.id_pregunta.all()])

	def get_respuesta(self):
		return "\n".join([p.nombre for p in self.id_respuesta.all()])

class examen(models.Model):
	id_examen = models.AutoField(primary_key=True)
	id_materia = models.ForeignKey(materia,related_name="idmate")
	id_alumno = models.ForeignKey(alumno,null=True,blank=True)
	unidad = models.IntegerField()
	id_pregunta_respuesta = models.ManyToManyField(pregunta_respuesta)

	def __unicode__(self):
		return '%s'%(self.id_examen)

	def get_pregunta_respuesta(self):
		return "\n".join([str(p.id_pregunta_respuesta) for p in self.id_pregunta_respuesta.all()])

	class Meta:
		unique_together = ('id_materia','unidad')
