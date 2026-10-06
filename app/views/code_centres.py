from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Code_centre
from app.forms import Code_centreForm

def index(request):
    assert isinstance(request, HttpRequest)
    code_centres = Code_centre.objects.all()
    return render(
        request,
        'app/agent_de_saisie/templates/CodeCentre/index.html',
        {
            'code_centres': code_centres
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = Code_centreForm()
        
    return render(
        request, 
        'app/agent_de_saisie/templates/CodeCentre/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = Code_centreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le code centre a été enregistré avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/agent_de_saisie/templates/CodeCentre')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = Code_centreForm(request.POST)
        else:
            category = Code_centre.objects.get(pk=id)
            form = Code_centreForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "Le code centre a été modifié avec succès !")
        return redirect('/agent_de_saisie/templates/CodeCentre')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = Code_centreForm()
        else:
            code_centre = Code_centre.objects.get(pk=id)
            form = Code_centreForm(instance=code_centre)
        return render(
            request,
            'app/agent_de_saisie/templates/CodeCentre/edit.html',
            {
                'form': form,
            }
        )

def delete(request, id):
    code_centre = Code_centre.objects.get(pk=id)
    code_centre.delete()
    messages.success(request, "Le code centre a été supprimé avec succès !")
    return redirect('/agent_de_saisie/templates/CodeCentre')

 
    