from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import maestro, alumno, pregunta_respuesta, examen, materia, alumno_materia, pregunta, respuesta
from django.forms import ModelMultipleChoiceField

class UserForm(UserCreationForm):
	n_empleado = forms.CharField(max_length=64)
	nombre = forms.CharField(max_length=64)
	correo = forms.CharField(max_length=64)

class estudianteForm(UserCreationForm):
	n_control = forms.CharField(max_length=8)
	nombre = forms.CharField(max_length=64)
	apellido = forms.CharField(max_length=64)
	correo = forms.CharField(max_length=64)

class materiaForm(forms.ModelForm):
	#serie = forms.CharField(max_length=64)
	#nombre = forms.CharField(max_length=64)
	#maestro_a = forms.CharField(max_length=64)
	class Meta:
		model = materia
		#fields = ('serie','nombre','maestro_a')
		exclude = ['maestro_a']

class alumno_materiaForm(forms.ModelForm):
	class Meta:
		model = alumno_materia
		fields = '__all__'

class preguntaForm(forms.ModelForm):
	class Meta:
		model = pregunta
		fields = '__all__'

class respuestaForm(forms.ModelForm):
	class Meta:
		model = respuesta
		fields = '__all__'

class pregunta_respuestaForm(forms.ModelForm):
	class Meta:
		model = pregunta_respuesta
		fields = '__all__'

class examenForm(forms.ModelForm):
	class Meta:
		model = examen
		fields = '__all__'
		
