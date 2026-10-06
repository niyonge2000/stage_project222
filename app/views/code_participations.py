from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Code_participation
from app.forms import Code_participationForm

def index(request):
    assert isinstance(request, HttpRequest)
    code_participations = Code_participation.objects.all()
    return render(
        request,
        'app/agent_de_saisie/templates/CodeParticipation/index.html',
        {
            'code_participations': code_participations
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = Code_participationForm()
        
    return render(
        request, 
        'app/agent_de_saisie/templates/CodeParticipation/add.html',
        {
            'form': form
        }
    )

def store(request):
    if request.method == 'POST':
        form = Code_participationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le code  a été enregistré avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/agent_de_saisie/templates/CodeParticipation')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = Code_participationForm(request.POST)
        else:
            category = Code_participation.objects.get(pk=id)
            form = Code_participationForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "Le code a été modifié avec succès !")
        return redirect('/agent_de_saisie/templates/CodeParticipation')
    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = Code_participationForm()
        else:
            code_participation = Code_participation.objects.get(pk=id)
            form = Code_participationForm(instance=code_participation)
        return render(
            request,
            'app/agent_de_saisie/templates/CodeParticipation/edit.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    code_participation = Code_participation.objects.get(pk=id)
    code_participation.delete()
    messages.success(request, "Le code a été supprimé avec succès !")
    return redirect('/agent_de_saisie/templates/CodeParticipation')

 

