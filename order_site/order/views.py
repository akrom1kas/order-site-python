from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("Labas, pasauli!")

def homepage(request):
    return render(request, "homepage.html")