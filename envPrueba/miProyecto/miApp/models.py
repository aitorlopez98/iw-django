from django.db import models

# Create your models here.

class Departamento(models.Model):
    #No es necesario crear Primary Key, Django crea un IntegerField por defecto.
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}, telefono={self.telefono}"

class Especializacion(models.Model):
    #No es necesario crear Primary Key, Django crea un IntegerField por defecto.
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}"

class Empleado(models.Model):
    #Campo relacion one to many.
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    especialidad = models.ManyToManyField(Especializacion)
    nombre = models.CharField(max_length=40)
    f_nacimiento = models.DateField()
    #Inicia a 0 (Valor por defecto)
    antiguedad = models.IntegerField(default=0)

    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}, fecha_nacimiento={self.f_nacimiento}, antigüedad={self.antiguedad}"
