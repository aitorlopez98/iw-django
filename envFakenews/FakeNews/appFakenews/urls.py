from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noticias/', views.NoticiasListView.as_view(), name='noticias'),
    path('noticia/<int:pk>', views.NoticiaDetailView.as_view(), name='noticia_det'),
    path('categorias/', views.CategoriasListView.as_view(), name='categorias'),
    path('cnoticia/', views.CreateNoticiaView.as_view(), name='create_noticia_form'),
]
