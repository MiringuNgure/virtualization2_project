from django.shortcuts import render
from .models import Airport_data

def index(request):
    results = Airport_data.objects.all()
    return render(request, "index.html", {"data":results})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html") 