from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views import View
from .models import Departamento, Empleado, Especializacion
from django.http import HttpResponse
from .forms import EmpleadoForm


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
    nombre = request.POST["nombre"]
    apellidos = request.POST["apellidos"]
    edad = request.POST["edad"]
    email = request.POST["email"]
    direccion = request.POST["direccion"]
    return HttpResponse(f"{nombre} --- {apellidos} --- {edad} --- {email} --- {direccion}")

def show_empleado_form(request):
    form = EmpleadoForm()
    return render(request, 'empleado_form.html', {'form': form})

def post_empleado_form(request):
    form = EmpleadoForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        edad = form.cleaned_data['edad']
        email = form.cleaned_data['email']
        direccion = form.cleaned_data['direccion']
        return HttpResponse(f"El nombre es: {nombre} {apellidos}, {edad}, {email}, {direccion}")

class CreateEmpleadoView(View):
    def get(self, request, *args, **kwargs):
        form = EmpleadoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear empleado'
                   }
        return render(request, 'empleado_form.html', context)

    def post(self, request, *args, **kwargs):
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleados')

        return render(request, 'empleado_form.html', {'form': form})
