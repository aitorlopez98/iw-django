from django import forms
from .models import Empleado, Departamento, Especializacion

class EmpleadoForm(forms.ModelForm):
    # nombre = forms.CharField(label='Nombre', max_length=100)
    # apellidos = forms.CharField(label='Apellidos', max_length=150)
    # edad = forms.IntegerField(label='Edad')
    # email = forms.EmailField(label='Email', required=False)
    # direccion = forms.CharField(label='Direccion')

    class Meta:
        model = Empleado
        fields = '__all__'
