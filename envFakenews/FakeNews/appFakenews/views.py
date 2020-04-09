from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria, Noticia
from django.views. generic import ListView, DetailView
from django.views import View
from .forms import NoticiaForm, CategoriaForm

# Create your views here.
def index(request):
    context = {'mensaje': 'BIENVENIDO A LA APP'}
    return render(request, 'index.html', context)

class NoticiasListView(ListView):
    model = Noticia
    template_name = 'noticias.html'
    queryset = Noticia.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(NoticiasListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Noticias falsas existentes'
        return context

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticia.html'

    def get_context_data(self, **kwargs):
        context = super(NoticiaDetailView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Noticias falsas detalladas'
        return context

class CategoriasListView(ListView):
    model = Categoria
    template_name = 'categorias.html'
    queryset = Categoria.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(CategoriasListView, self).get_context_data(**kwargs)
        context['titulo_pagina'] = 'Categorias existentes'
        return context

class CreateNoticiaView(View):
    def get(self, request, *args, **kwargs):
        form = NoticiaForm()
        context = {
            'form': form,
            'titulo_pagina': 'Crear Noticia'
        }
        return render(request, 'create_noticia_form.html', context)

    def post(self, request, *args, **kwargs):
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noticias')

        return render(request, 'create_noticia_form.html', {'form': form})
