from django.shortcuts import render

# Create your views here.
def sample_app(request):
    return render(request, 'sample_app.html', {})