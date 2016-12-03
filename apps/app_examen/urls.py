from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
	url(r'^$',login,{'template_name':'app_examen/index.html'}, name='login'),
	url(r'^logout/$', logout_then_login, name='logout'),
	url(r'^$',index_view,name='index_view'),
	url(r'^registro_materia/$',registro_materia.as_view(),name='registro_materia'),
	url(r'^registro_maestro/$',registro_maestro.as_view(),name='registro_maestro'),
	url(r'^listado_materias/$',listado_materias,name='listado_materias'),
	url(r'^registro_alumno/$',registro_alumno.as_view(),name='registro_alumno'),
	url(r'^detalle_materia/(?P<pk>[-\w]+)/$',detalle_materia,name='detalle_materia'),
	url(r'^anadir_pregunta/(?P<pk>[-\w]+)/$',anadir_pregunta,name='anadir_pregunta'),
	url(r'^generar_examen/(?P<pk>[-\w]+)/$',generar_examen,name='crear_examen'),
	url(r'^anadir_respuesta/$',anadir_respuesta,name='anadir_respuesta'),
]