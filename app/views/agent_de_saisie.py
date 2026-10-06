from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Etudiant,Code_centre,Code_ecole,Laureats

def index(request):
    assert isinstance(request, HttpRequest)
    etudiants = Etudiant.objects.all().count()
    code_centres = Code_centre.objects.all().count()
    code_ecoles = Code_ecole.objects.all().count()
    laureates = Laureats.objects.all().count()
    return render(
        request,
        'app/agent_de_saisie/home/index.html',
        {
            'etudiants': etudiants,
            'code_centres': code_centres,
            'code_ecoles': code_ecoles,
            'laureates': laureates
        }
    )