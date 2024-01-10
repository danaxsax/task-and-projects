# define que se envia al cliente (html)
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject


#funcion nombre(parametros)
def home(request):
   #declaracion de variables
   title = "Django course!!!"
   #              (parametro1, parametro2, diccionario que manda variables)
   return render (request, "index. html", {
      "title" : title 
   })

def about(request):
   username = "Danaxsax"
   return render(request, "about.html", {
      "username" : username
   })
    
def projects(request):
   #lo mismo que se hizo en el shell .all() 
   projects = Project.objects.all()
   return render(request, "projects/projects.html", {
      "projects" : projects,
   })

def tasks(request):
   tasks = Task.objects.all()
   return render(request,"tasks/tasks.html", {
      "tasks" : tasks,
   })
   
def create_task(request):
   if request.method == "GET":
      # muestra inferfaz
      return render(request, "tasks/create_task.html", {
      "form": CreateNewTask()
      })
   else:
      Task.objects.create(title = request.POST['title'], description = request.POST['description'], project_id= 2)
      return redirect("tasks")
   
def create_project(request):
   if request.method=="GET":
      return render(request, "projects/create_project.html",{
         "form" : CreateNewProject()
      })
   else: 
      Project.objects.create(name = request.POST['name'])
      return redirect("projects")

def project_detail(request,id):
   project = get_object_or_404(Project, id=id)
   task = Task.objects.filter(project_id = id)
   return render (request, "projects/detail.html", {
      "project" : project,
      "task" : task,
   })
   

