from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "homepage/home.html")
def index(request):
    return render(request, "homepage/index.html")
def about(request):
    return render(request, "homepage/about.html")
def notes(request):
    return render(request, "homepage/notes.html")
def notFound(request):
    return render(request, "homepage/notFound.html")