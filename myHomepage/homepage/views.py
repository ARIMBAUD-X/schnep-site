from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "homepage/index.html")
def about(request):
    return render(request, "homepage/about.html")
def notes(request):
    return render(request, "homepage/notes.html")
def notFound(request):
    return render(request, "homepage/not_found.html")