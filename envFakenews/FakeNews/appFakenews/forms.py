from django import forms
from .models import Noticia, Categoria

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
