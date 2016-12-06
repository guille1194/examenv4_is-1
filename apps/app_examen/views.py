from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import FormView, CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import UserForm, estudianteForm, materiaForm, alumno_materiaForm, preguntaForm, respuestaForm, pregunta_respuestaForm, examenForm, realizar_examenForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import realizar_examen, maestro, materia, alumno, alumno_materia, pregunta, respuesta, pregunta_respuesta, examen
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import User
from django.views.generic.edit import ModelFormMixin
# Create your views here.

def index_view(request):
	return render(request,'app_examen/index.html')

class registro_maestro(FormView):
	template_name = 'app_examen/registro_maestro.html'
	form_class = UserForm
	success_url = reverse_lazy('index_view')

	def form_valid(self,form):
		user = form.save()
		p = maestro()
		p.user_perfil = user
		p.n_empleado = form.cleaned_data['n_empleado']
		p.nombre = form.cleaned_data['nombre']
		p.correo = form.cleaned_data['correo']
		p.save()
		return super(registro_maestro,self).form_valid(form)

class registro_alumno(FormView):
	template_name = 'app_examen/registro_alumno.html'
	form_class = estudianteForm
	success_url = reverse_lazy('index_view')

	def form_valid(self,form):
		user = form.save()
		p = alumno()
		p.user_perfil = user
		p.n_control = form.cleaned_data['n_control']
		p.nombre = form.cleaned_data['nombre']
		p.apellido = form.cleaned_data['apellido']
		p.correo = form.cleaned_data['correo']
		p.save()
		return super(registro_alumno,self).form_valid(form)

def listado_materias(request):
	current_user = request.user.profile.n_empleado
	materias = materia.objects.filter(maestro_a = current_user)
	ctx = {'materias':materias,}
	return render(request,'app_examen/listado_materias.html',ctx)

#def registro_materia(request):
	#instace_maestro = get_object_or_404(maestro,n_empleado="cafj940201hbclls09")
#	profe = maestro.objects.get(n_empleado = request.POST['maestro_a'])
#	form=materiaForm(request.POST or None)
#	ctx = {
#		"form":form
#	}
#	if form.is_valid:
#		instace = form.save(commit=False)
#		instace.maestro_a = profe
#		instace.save()
#		return redirect('registro_materia')

#	return render(request,'app_examen/registro_materia.html',ctx)

class registro_materia(CreateView):
	template_name = 'app_examen/registro_materia.html'
	model = materia
	fields = ['serie','nombre','maestro_a']
	success_url = reverse_lazy('index_view')

	def post(self, request, *args, **kwargs):
		flag = False
		p = materia()
		query = materia.objects.filter(serie = request.POST['serie'])
		if query:
			if query.count == 1:
				flag = False
		else:
			a = request.POST['maestro_a']
			user = maestro.objects.get(n_empleado=a)
			print user
			p.serie = request.POST['serie']
			p.nombre = request.POST['nombre']
			p.maestro_a = user
			p.save()

		return redirect('index_view')

def detalle_materia(request,pk):
	insta = get_object_or_404(materia,serie=pk)
	ctx = {"object":insta}
	form = alumno_materiaForm(request.POST or None)
	try:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.alum = alumno.objects.get(n_control = request.POST['alum'])
			instance.materi = materia.objects.get(serie = request.POST['materi'])
			instance.save()
			return redirect('index_view')
	except:
			print "error"
	return render(request,'app_examen/detalle_materia.html',ctx)

def anadir_pregunta(request,pk=None):
	insta = get_object_or_404(materia,serie=pk)
	ctx = {"object":insta}
	form = preguntaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.materia = materia.objects.get(serie = request.POST['materia'])
		instance.save()
		return redirect('anadir_respuesta')
		#return render_to_response('anadir_respuesta/pregunta_get')

	return render(request,'app_examen/anadir_pregunta.html',ctx)

def anadir_respuesta(request,pk=None):
	pregunta_get = pregunta.objects.latest('id')
	respuesta_get = respuesta.objects.latest('id')
	form = respuestaForm(request.POST or None)
	form2 = pregunta_respuestaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.pregun = pregunta.objects.get(id=request.POST['pregun'])
		instance.nombre = request.POST['nombre']
		instance.save()
		p = pregunta_respuesta()
		p.id_pregunta = instance.pregun 
		p.save()
		p.id_respuesta.add(respuesta_get)
	else:
		print 'error en captura de pregunta'
	return render(request,'app_examen/respuesta.html',{"object":pregunta_get})


def generar_examen(request,pk):
	form = examenForm(request.POST or None)
	insta = get_object_or_404(materia,serie=pk)
	pregunta_res = pregunta_respuesta.objects.all()
	ctx = {
		'object':insta,
		'pregunta_res':pregunta_res,
		'form':form,
	}

	context = {}
	print pregunta_res
	if 'id_respuesta' in request.GET:
		context['id_respuesta'] = request.GET.get('id_respuesta')
		return context
		#print context

	i = 0
	for i in context.items():
		i += 1
		#print i 
		return i
	
	if form.is_valid():
		instance = form.save()
		instance.id_materia = materia.objects.get(serie = request.POST['id_materia'])
		#instance.id_pregunta_respuesta = pregunta_respuesta.objects.get(id_pregunta_respuesta=request.POST['id_pregunta_respuesta']).values()
		#print instance.id_pregunta_respuesta
		instance.save()
	return render(request,'app_examen/crear_examen.html',ctx)

def materias_alumno(request):
	current_user = request.user.alumno.n_control
	a_m = alumno_materia.objects.filter(alum = current_user)
	ctx = {'a_m':a_m,}
	#print a_m
	return render(request,'app_examen/materias_alumno.html',ctx)

def detalle_examen(request,pk=None):
	insta = get_object_or_404(materia,serie=pk)
	current_user = request.user.alumno.n_control
	queryset_list = examen.objects.all()
	queryset_list2 = alumno_materia.objects.filter(alum = current_user)
	ctx = {
		"object":insta,
		"object_list": queryset_list,
		"object_list2":queryset_list2,
	}
	return render(request,'app_examen/detalle_examen.html',ctx)

def realizar_examene(request,pk=None):
	insta = get_object_or_404(examen,id_examen=pk)
	current_user = request.user.alumno.n_control
	queryset_list = examen.objects.filter(id_examen = insta.id_examen)
	queryset_list2 = realizar_examen.objects.filter(id_examen = insta.id_examen)
	form = realizar_examenForm(request.POST or None)
	guess = request.POST.get('id_respuesta')
    #is_correct = self.question.check_if_correct(guess)
    
	#print guess
	ctx = {
		"object":insta,
		"object_list": queryset_list,
		"object_list2":queryset_list2,
		"form":form,
	}
	context = {}
	if 'id_respuesta' in request.GET:
		context['id_respuesta'] = request.GET.get('id_respuesta')
	context['id_respuesta'] = request.GET.get('id_respuesta')

	r_corectas = respuesta.objects.filter(correcta = True)
	promedio = 0
	print promedio
	lista = []
	lista2 = []
	for i in r_corectas:
		lista.append(i.id)
	respuestas = realizar_examen.objects.filter(id_examen=pk)
	if form.is_valid():
		instance = form.save()
		instance.save()
		for l in request.POST.getlist('id_respuesta'):
			lista2.append(l)
			print "ok"



		
		
		
		return redirect('index_view')

	return render(request,'app_examen/realizar_examen.html',ctx)


