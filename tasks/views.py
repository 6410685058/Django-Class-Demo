from django.shortcuts import render
import django.http import HttpResponse
import django.urls import reverse
import django. import from
tasks = ['tasks 1', 'tasks 2','tasks 3']
# Create your views here.

def index(request):
    return render()

class NewTaskFrom(froms.for):


def add(request):
    if request_method = 'POST':
        form = NewTaskFrom(request.POST)
        if form.is_V
        task = request.POST['tast']
        tasks.append(task)
