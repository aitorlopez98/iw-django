from django.contrib import admin
from .models import Departamento, Empleado, Especializacion

# Register your models here.
admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Especializacion)
