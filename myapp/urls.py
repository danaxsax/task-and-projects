from django.urls import path
from . import views # o from myapp.views import hello (en este caso solo llamas al hello, no a todo el contenido de views)
urlpatterns = [
        #despues recibe string:usuarios
    path('', views.home, name="home"),
    path('about/', views.about, name = "about"),
    path('projects/', views.projects, name="projects" ),
    path('projects/<int:id>', views.project_detail, name="project_detail" ),
    path('tasks/', views.tasks, name="tasks" ),
    path('create_task/', views.create_task , name="create_task" ),
    path('create_project/', views.create_project, name="create_project" ),
]
 