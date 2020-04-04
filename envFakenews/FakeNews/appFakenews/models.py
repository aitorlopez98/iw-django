from django.db import models

# Create your models here.

class Categoria(models.Model):
    #No es necesario crear Primary Key, Django crea un IntegerField por defecto.
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"Categoria: {self.nombre}"

class Noticia(models.Model):
    #No es necesario crear Primary Key, Django crea un IntegerField por defecto.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titular = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    medio = models.CharField(max_length=50)
    enlace = models.CharField(max_length=200)
    f_publi = models.DateField()


    def __str__(self):
        return f"{self.categoria}, Titular: {self.titular}, Descipcion: {self.desc}, Medio publicacion: {self.medio}, Enlace: {self.enlace}, Fecha publicacion: {self.f_publi}"
