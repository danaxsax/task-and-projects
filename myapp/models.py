# Crear modelos (tablas de sql) con palabra reservada classs mediante migraciones 
from django.db import models

class Project(models.Model): #nombre de la clase (herencia)
                #CharField - texto
    name = models.CharField(max_length= 30) #atributo = modelo.tipo de dato (longitud)
    
    #configuracion para mostrar nombre en el admin
    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length = 400)
    #               claveforanea(class q pertenece la key. on_delete=encaso de bottar el project, las task relacionadas se eliminan tmbn )
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    done = models.BooleanField(default=False)
    #configuracion para mostrar nombre en el admin
    def __str__(self) -> str:
                        #concatenas
        return self.title + " - " + self.project.name


