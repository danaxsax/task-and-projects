#formularios, permite extender caracteristicas de una clase 
from django import forms

class CreateNewTask(forms.Form):
    #envia info al html y lo convierte en texto
    title = forms.CharField(label='titulo de tarea', max_length=40)
    description = forms.CharField(label='descripcion tarea', widget=forms.Textarea, max_length=400)

class CreateNewProject(forms.Form):
    name = forms.CharField(label= 'nombre del proyecto', max_length= 30)
