from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Noticia
from django.views. generic import ListView, DetailView

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
