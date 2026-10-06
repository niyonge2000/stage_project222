from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages


from app.models import Laureats
from app.forms import LaureatsForm


def index(request):
    assert isinstance(request, HttpRequest)
    laureates= Laureats.objects.all()
    return render(
        request,
        'app/agent_de_saisie/templates/laureates/index.html',
        {
            'laureates': laureates
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = LaureatsForm()
        
    return render(
        request, 
        'app/agent_de_saisie/templates/laureates/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = LaureatsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Le laureat' a été enregistré avec succès !")
        else :
            messages.success(request, form.errors)
        return redirect('/agent_de_saisie/templates/laureates')
    
def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = LaureatsForm(request.POST)
        else:
            category = Laureats.objects.get(pk=id)
            form = LaureatsForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "Le laureat' a été modifié avec succès !")
        return redirect('/agent_de_saisie/templates/laureates')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = LaureatsForm()
        else:
            laureats = Laureats.objects.get(pk=id)
            form = LaureatsForm(instance=laureats)
        return render(
            request,
            'app/agent_de_saisie/templates/laureates/edit.html',
            {
                'form': form,
            }
        )
    
def delete(request, id):
    laureats = Laureats.objects.get(pk=id)
    laureats.delete()
    messages.success(request, "le laureat a été supprimé avec succès !")
    return redirect('/agent_de_saisie/templates/laureates')
        




  