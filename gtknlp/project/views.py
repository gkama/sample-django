from django.shortcuts import render
from project.models import Project

def project_index(request):
    p1 = Project(
        title='My First Project',
        description='A web development project.',
        technology='Django',
        image='img/project1.png'
        )
    p2 = Project(
        title='My Second Project',
        description='A web development project.',
        technology='Django',
        image='img/project1.png'
    )

    projects = [p1, p2]

    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)