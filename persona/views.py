from django.shortcuts import render

# Create your views here.
def persona(request):
    return render(request, 'persona.html', {})