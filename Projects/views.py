from django.shortcuts import render
from .models import Project

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'Projects/projects.html', context)
def content(request, slug):
    project = Project.objects.filter(slug=slug).first()
    context = {'project':project}
    return render(request, 'Projects/content.html', context)
