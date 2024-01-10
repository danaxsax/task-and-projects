# Crear modelos (tablas de sql) con palabra reservada class mediante migraciones 
from django.db import models
from datetime import date

class Project(models.Model): #nombre de la clase (herencia)
                #CharField - texto
    name = models.CharField(max_length= 30) #atributo = modelo.tipo de dato (longitud)
    #configuracion para mostrar nombre en el admin
    date = models.DateField(default =date.today() )
    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length = 400)
    #               claveforanea(class q pertenece la key. on_delete=en caso de bottar el project, las task relacionadas se eliminan tmbn )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name= "main project+") 
    done = models.BooleanField(default=False)
    #configuracion para mostrar nombre en el admin
    def __str__(self) -> str:
                        #concatenas
        return self.title + " - " + self.project.name


