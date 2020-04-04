from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos/', views.DepartamentosListView.as_view(), name='departamentos'),
    path('departamento/<int:pk>', views.DepartamentoDetailView.as_view(), name='dep_detail'),
    path('empleado/<int:pk>/', views.EmpleadoDetailView.as_view(), name='emp_detail'),
    path('empleados/', views.EmpleadosListView.as_view(), name='empleados'),
    path('registro/', views.show_form, name='registro'),
    path('registrar/', views.post_form, name='registrar')
]
