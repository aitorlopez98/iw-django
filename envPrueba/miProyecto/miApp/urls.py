from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos', views.departamentos, name='departamentos'),
    path('departamento/<int:departamento_id>', views.departamento, name='dep_detail'),
    path('empleado/<int:empleado_id>', views.empleado, name='emp_detail'),
    path('empleados', views.empleados, name='empleados')
]
