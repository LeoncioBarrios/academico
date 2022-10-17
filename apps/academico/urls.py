from django.urls import path

from .views import alumnos_listar, alumnos_agregar, alumnos_editar, alumnos_eliminar
from .views import docentes_listar, docentes_agregar, docentes_editar, docentes_eliminar
from .views import sis_evaluacion_listar, sis_evaluacion_agregar, sis_evaluacion_editar, sis_evaluacion_eliminar
from .views import cursos_listar, cursos_agregar, cursos_editar, cursos_eliminar
from .views import ciclos_listar, ciclos_agregar, ciclos_editar, ciclos_eliminar


urlpatterns = [
	path('alumnos_listar/', alumnos_listar, name='alumnos_listar'),
	path('alumnos_agregar/', alumnos_agregar, name="alumnos_agregar"),
	path('alumnos_editar/<int:id>/', alumnos_editar, name="alumnos_editar"),
	path('alumnos_eliminar/<int:id>/', alumnos_eliminar, name="alumnos_eliminar"),
	
	path('docentes_listar/', docentes_listar, name='docentes_listar'),
	path('docentes_agregar/', docentes_agregar, name='docentes_agregar'),
	path('docentes_editar/<int:id>/', docentes_editar, name='docentes_editar'),
	path('docentes_eliminar/<int:id>/', docentes_eliminar, name='docentes_eliminar'),
	
	path('sis_evaluacion_listar/', sis_evaluacion_listar, name='sis_evaluacion_listar'),
	path('sis_evaluacion_agregar/', sis_evaluacion_agregar, name='sis_evaluacion_agregar'),
	path('sis_evaluacion_editar/<int:id>/', sis_evaluacion_editar, name='sis_evaluacion_editar'),
	path('sis_evaluacion_eliminar/<int:id>/', sis_evaluacion_eliminar, name='sis_evaluacion_eliminar'),
	
	path('cursos_listar/', cursos_listar, name='cursos_listar'),
	path('cursos_agregar/', cursos_agregar, name='cursos_agregar'),
	path('cursos_editar/<int:id>/', cursos_editar, name='cursos_editar'),
	path('cursos_eliminar/<int:id>/', cursos_eliminar, name='cursos_eliminar'),
	
	path('ciclos_listar/', ciclos_listar, name='ciclos_listar'),
	path('ciclos_agregr', ciclos_agregar, name='ciclos_agregar'),
	path('ciclos_editar/<int:id>/', ciclos_editar, name='ciclos_editar'),
	path('ciclos_eliminar/<int:id>/', ciclos_eliminar, name='ciclos_eliminar'),
]