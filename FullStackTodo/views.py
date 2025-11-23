from django.shortcuts import render
from todo.models import Task
def home(req):
    task=Task.objects.filter(is_completed=False)
    print(task)
    return render(req,"home.html",{'tasks':task})
