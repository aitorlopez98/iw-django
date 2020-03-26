from django.shortcuts import render
from .models import Departamento

# Create your views here.

from django.http import HttpResponse

#Devuelve todos los departamentos
def departamentos(request):
    departamentos = Departamento.objects.order_by('id')
    context = {'titulo_pagina': 'Departamentos existentes', 'lista_departamentos' : departamentos}
    return render(request, 'departamentos.html', context)

#Devuelve los datos de un departamento por ID
def departamento(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    context = {'titulo_pagina': 'Detalles por departamento', 'departamento': departamento}
    return render(request, 'departamento.html', context)

#Devuelve todos los empleados
def empleados(request):
    empleados = Empleado.objects.order_by('id')
    context = {'titulo_pagina': 'Empleados existentes', 'lista_empleados': empleados}
    return render(request, 'empleados.html', context)

#Devuelve los datos de un empleado por ID
def empleado(request, empleado_id):
    empleado = Empleado.objects.get(pk=empleado_id)
    context = {'titulo_pagina': 'Detalles por empleado', 'empleado': empleado}
    return render(request, 'empleado.html', context)
