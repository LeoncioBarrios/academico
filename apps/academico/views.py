from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from datetime import date

from .models import Alumnos, Docentes, SistemaEvaluacion, Cursos, CiclosAcademicos
from .forms import AlumnosForm, DocentesForm, SistemaEvaluacionForm, CursosForm, CiclosForm

#=====================================================================================================================
def inicio(request):
	return render(request, 'inicio.html', {'fecha':date.today()})


#-- Alumnos ----------------------------------------------------------------------------------------------------------
def alumnos_listar(request):
	#alumnos = Alumnos.objects.all()
	alumnos_paginados = Paginator(Alumnos.objects.all(), 7)  # El objeto paginado "paginator"
	page = request.GET.get('page',1)
	alumnos = alumnos_paginados.get_page(page)  # El objeto "page_obj"
	return render(request, 'academico/alumnos_listar.html', {'data':alumnos, 'paginator':alumnos_paginados})
	

def alumnos_agregar(request):
	if request.method == 'POST':
		form = AlumnosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('alumnos_listar')
	else:
		form = AlumnosForm()
	return render(request, 'academico/alumnos_form.html', {'form':form, 'otro':'Leoncio'})

def alumnos_editar(request, id):
	alumno = Alumnos.objects.get(id=id)
	if request.method == 'GET':
		form = AlumnosForm(instance=alumno)
	else:
		form = AlumnosForm(request.POST, instance=alumno)
		if form.is_valid():
			form.save()
		return redirect('alumnos_listar')
	return render(request, 'academico/alumnos_form.html', {'form':form})

def alumnos_eliminar(request, id):
	alumno = Alumnos.objects.get(id=id)
	if request.method == 'POST':
		alumno.delete()
		return redirect('alumnos_listar')
	return render(request, 'academico/alumnos_eliminar.html', {'alumno':alumno})

#-- Docentes ----------------------------------------------------------------------------------------------------------
def docentes_listar(request):
	docentes_paginados = Paginator(Docentes.objects.all(), 7)  # Paginator
	page = request.GET.get('page',1)
	docentes = docentes_paginados.get_page(page)  # page_obj
	return render(request, 'academico/docentes_listar.html', {'data':docentes, 'paginator':docentes_paginados})

def docentes_agregar(request):
	if request.method == 'POST':
		form = DocentesForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('docentes_listar')
	else:
		form = DocentesForm()
	return render(request, 'academico/docentes_form.html', {'form':form})

def docentes_editar(request, id):
	docente = Docentes.objects.get(id=id)
	if request.method == 'GET':
		form = DocentesForm(instance=docente)
	else:
		form = DocentesForm(request.POST, instance=docente)
		if form.is_valid():
			form.save()
		return redirect('docentes_listar')
	return render(request, 'academico/docentes_form.html', {'form':form})

def docentes_eliminar(request, id):
	docente = Docentes.objects.get(id=id)
	if request.method == 'POST':
		docente.delete()
		return redirect('docentes_listar')
	return render(request, 'academico/docentes_eliminar.html', {'docente':docente})

#-- Sistemas de Evaluación -------------------------------------------------------------------------------------------
def sis_evaluacion_listar(request):
	#sis_evals = SistemaEvaluacion.objects.all()
	sis_eval_paginados = Paginator(SistemaEvaluacion.objects.all(), 5)  # Paginator
	page = request.GET.get('page', 1)
	sis_evals = sis_eval_paginados.get_page(page)  # page_obj
	return render(request, 'academico/sis_evaluacion_listar.html', {'data':sis_evals, 'paginator':sis_eval_paginados})

def sis_evaluacion_agregar(request):
	if request.method == 'POST':
		form = SistemaEvaluacionForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('sis_evaluacion_listar')
	else:
		form = SistemaEvaluacionForm()
	return render(request, 'academico/sis_eval_form.html', {'form':form})

def sis_evaluacion_editar(request, id):
	sis_eval = SistemaEvaluacion.objects.get(id=id)
	if request.method == 'GET':
		form = SistemaEvaluacionForm(instance=sis_eval)
	else:
		form = SistemaEvaluacionForm(request.POST, instance=sis_eval)
		if form.is_valid():
			form.save()
		return redirect('sis_evaluacion_listar')
	return render(request, 'academico/sis_eval_form.html', {'form':form})

def sis_evaluacion_eliminar(request, id):
	sis_eval = SistemaEvaluacion.objects.get(id=id)
	if request.method == 'POST':
		sis_eval.delete()
		return redirect('sis_evaluacion_listar')
	return render(request, 'academico/sis_evaluacion_eliminar.html', {'sis_eval':sis_eval})

#-- Cursos -----------------------------------------------------------------------------------------------------------
def cursos_listar(request):
	cursos_paginados = Paginator(Cursos.objects.all(), 5)
	page = request.GET.get('page', 1)
	cursos = cursos_paginados.get_page(page)
	return render(request, 'academico/cursos_listar.html', {'data':cursos, 'paginator':cursos_paginados})

def cursos_agregar(request):
	if request.method == 'POST':
		form = CursosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('cursos_listar')
	else:
		form = CursosForm()
	return render(request, 'academico/cursos_form.html', {'form':form})

def cursos_editar(request, id):
	curso = Cursos.objects.get(id=id)
	if request.method == 'GET':
		form = CursosForm(instance=curso)
	else:
		form = CursosForm(request.POST, instance=curso)
		if form.is_valid():
			form.save()
		return redirect('cursos_listar')
	return render(request, 'academico/cursos_form.html', {'form':form})

def cursos_eliminar(request, id):
	curso = Cursos.objects.get(id=id)
	if request.method == 'POST':
		curso.delete()
		return redirect('cursos_listar')
	return render(request, 'academico/cursos_eliminar.html', {'curso':curso})

#-- Ciclos Académicos ------------------------------------------------------------------------------------------------
def ciclos_listar(request):
	ciclos_paginados = Paginator(CiclosAcademicos.objects.all(), 5)
	page = request.GET.get('page', 1)
	ciclos = ciclos_paginados.get_page(page)
	return render(request, 'academico/ciclos_listar.html', {'data':ciclos, 'paginator':ciclos_paginados})
	
def ciclos_agregar(request):
	if request.method == 'POST':
		form = CiclosForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('ciclos_listar')
	else:
		form = CiclosForm()
	return render(request, 'academico/ciclos_form.html', {'form':form})
	
def ciclos_editar(request, id):
	ciclo = CiclosAcademicos.objects.get(id=id)
	if request.method == 'GET':
		form = CiclosForm(instance=ciclo)
	else:
		form = CiclosForm(request.POST, instance=ciclo)
		if form.is_valid():
			form.save()
		return redirect('ciclos_listar')
	return render(request, 'academico/ciclos_form.html', {'form':form})
	
def ciclos_eliminar(request, id):
	ciclo = CiclosAcademicos.objects.get(id=id)
	if request.method == 'POST':
		ciclo.delete()
		return redirect('ciclos_listar')
	return render(request, 'academico/ciclos_eliminar.html', {'ciclo':ciclo})

