from django.contrib import admin
from .models import realizar_examen, maestro, materia, alumno, alumno_materia, pregunta, respuesta, pregunta_respuesta, examen
# Register your models here.
@admin.register(maestro)
class maestro_admin(admin.ModelAdmin):
	list_display = ('n_empleado','user_perfil','nombre','correo','categoria')

@admin.register(materia)
class materia_admin(admin.ModelAdmin):
	list_display = ('serie','nombre','maestro_a')

@admin.register(alumno)
class alumno_admin(admin.ModelAdmin):
	list_display = ('n_control','nombre','apellido','correo')

@admin.register(alumno_materia)
class alumno_materia_admin(admin.ModelAdmin):
	list_display = ('id','alum','materi')

@admin.register(pregunta)
class pregunta_admin(admin.ModelAdmin):
	list_display = ('id','nombre','materia','semestre','dificultad','valor')

@admin.register(respuesta)
class respuesta_admin(admin.ModelAdmin):
	list_display = ('id','pregun','nombre','correcta')

@admin.register(pregunta_respuesta)
class pregunta_respuesta_admin(admin.ModelAdmin):
	list_display = ('id_pregunta_respuesta','id_pregunta','get_respuesta')

	


@admin.register(examen)
class examen_admin(admin.ModelAdmin):
	list_display = ('id_examen','id_materia','id_alumno','unidad','get_pregunta_respuesta')

@admin.register(realizar_examen)
class realizar_examen(admin.ModelAdmin):
	list_display = ('id','id_alumno','id_examen','get_pregunta_respuesta','get_respuesta','puntuacion')
