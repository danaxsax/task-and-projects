# registrar aplicaciones a panel de admin 

from django.contrib import admin
from .models import Project, Task
                    #anadio mi modelo Project y Task, previamente debi importarlos
admin.site.register(Project)
admin.site.register(Task)