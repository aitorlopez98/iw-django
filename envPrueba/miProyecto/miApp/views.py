from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Departamento, Empleado, Especializacion
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {'mensaje': 'BIENVENIDO A LA APP'}
    return render(request, 'index.html', context)

# Devuelve todos los departamentos
# def departamentos(request):
#     departamentos = Departamento.objects.order_by('id')
#     context = {'titulo_pagina': 'Departamentos existentes', 'lista_departamentos' : departamentos}
#     return render(request, 'departamentos.html', context)

class DepartamentosListView(ListView):
    model = Departamento
    template_name = 'departamentos.html'
    queryset = Departamento.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(DepartamentosListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Departamentos existentes'
        return context


#Devuelve los datos de un departamento por ID
# def departamento(request, departamento_id):
#     departamento = Departamento.objects.get(pk=departamento_id)
#     context = {'titulo_pagina': 'Detalles por departamento', 'departamento': departamento}
#     return render(request, 'departamento.html', context)

class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'departamento.html'

    def get_context_data(self, **kwargs):
        context = super(DepartamentoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles por departamento'
        return context

#Devuelve todos los empleados
# def empleados(request):
#     empleados = Empleado.objects.order_by('id')
#     context = {'titulo_pagina': 'Empleados existentes', 'lista_empleados': empleados}
#     return render(request, 'empleados.html', context)

class EmpleadosListView(ListView):
    model = Empleado
    template_name = 'empleados.html'
    queryset = Empleado.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(EmpleadosListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Empleados existentes'
        return context

#Devuelve los datos de un empleado por ID
# def empleado(request, empleado_id):
#     empleado = Empleado.objects.get(pk=empleado_id)
#     context = {'titulo_pagina': 'Detalles por empleado', 'empleado': empleado}
#     return render(request, 'empleado.html', context)

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Detalles por empleado'
        return context


def show_form(request):
    return render(request, 'registro.html')

def post_form(request):
    usuario = request.POST["usuario"]
    email = request.POST["email"]
    return HttpResponse(f"El usuario es {usuario} y el email es {email}")
