from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Code_ecole,Code_centre
from app.forms import Code_ecoleForm

def index(request):
    assert isinstance(request, HttpRequest)
    code_ecoles = Code_ecole.objects.all()
    return render(
        request,
        'app/agent_de_saisie/templates/CodeEcole/index.html',
        {
            'code_ecoles': code_ecoles
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = Code_ecoleForm()
        
    return render(
        request, 
        'app/agent_de_saisie/templates/CodeEcole/add.html',
        {
            'form': form
        }
    )
   
def store(request):
    if request.method == 'POST':
        form = Code_ecoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le code ecole a été enregistré avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/agent_de_saisie/templates/CodeEcole')

def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = Code_ecoleForm(request.POST)
        else:
            category = Code_ecole.objects.get(pk=id)
            form = Code_ecoleForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "Le code ecole a été modifié avec succès !")
        return redirect('/agent_de_saisie/templates/CodeEcole')
    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = Code_ecoleForm()
        else:
            code_ecole = Code_ecole.objects.get(pk=id)
            form = Code_ecoleForm(instance=code_ecole)
        return render(
            request,
            'app/agent_de_saisie/templates/CodeEcole/edit.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    code_ecole = Code_ecole.objects.get(pk=id)
    code_ecole.delete()
    messages.success(request, "Le code ecole a été supprimé avec succès !")
    return redirect('/agent_de_saisie/templates/CodeEcole')

def getCodeCentre(request):
    code_centre_id = request.GET.get('code_centre_id')
    code_ecoles = Code_ecole.objects.filter(code_centre_id = code_centre_id).order_by('nom')
    return render(
        request,
        'app/agent_de_saisie/templates/CodeEcole/getCodeCentre.html',
        {
            'code_ecoles':code_ecoles
        }
    )


  
