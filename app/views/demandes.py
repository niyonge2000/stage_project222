from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime, timedelta
import datetime
from django.core.mail import send_mail
from .mailsend import EmailConfirmation
from .rejetermail import Rejeter_mail


from app.models import Rendez_vous, Province, Code_centre, Code_ecole,Code_participation,Exetat
from app.forms import Rendez_vousForm


def index(request):
    assert isinstance(request, HttpRequest)
    demandes = Rendez_vous.objects.all()
    return render(
        request,
        'app/receptioniste/templates/demandes/index.html',
        {
            'demandes': demandes
        }
    )
    
def add(request):
    if request.method == 'GET' :
        form = Rendez_vousForm()
        
    return render(
        request, 
        'app/receptioniste/templates/demandes/add.html',
        {
            'form': form
            
        }
    )
    

    
# def store(request):
#     if request.method == 'POST':
#         form = Rendez_vousForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Votre demande a été envoyée avec succès !")
#         else :
#             messages.success(request, form.errors)
#         return redirect('/receptioniste/templates/demandes')
    
# def update(request, id):
#     if request.method == 'POST':
#         if id == 0:
#             form = Rendez_vousForm(request.POST)
#         else:
#             category = Rendez_vous.objects.get(pk=id)
#             form = Rendez_vousForm(request.POST, instance=category)
#         if form.is_valid():
#             form.save()
#         messages.success(request, "Votre demande a été modifiée avec succès !")
#         return redirect('/receptioniste/templates/demandes')

# def edit(request, id):
#     assert isinstance(request, HttpRequest)
#     if request.method == 'GET':
#         if id == 0:
#             form = Rendez_vousForm()
#         else:
#             rendez_vous = Rendez_vous.objects.get(pk=id)
#             form = Rendez_vousForm(instance=rendez_vous)
#         return render(
#             request,
#             'app/receptioniste/templates/demandes/add.html',
#             {
#                 'form': form,
#             }
#         )

# def delete(request, id):
#     rendez_vous = Rendez_vous.objects.get(pk=id)
#     rendez_vous.delete()
#     messages.success(request, "Votre demande a été supprimé avec succès !")
#     return redirect('/receptioniste/templates/demandes')


# approuver----demande
def date_generate ():
    dates = Rendez_vous.objects.values('date_delivrance')
    for i in range(0,len(dates)):
        date_delivrance = list(dates[i].values())[0]
    
    occurance = Rendez_vous.objects.filter(date_delivrance = date_delivrance).count()
    date = {}
    date[date_delivrance]=occurance
    return date

def test():
    dates = date_generate()
    if dates.values() <=9:
        pass
    else:
        pass
def ApprouverDemande(request, id):
    print("Approuver")
    assert isinstance(request, HttpRequest)
    demande=Rendez_vous.objects.filter(pk=id).first()
    demande.etat="Approuver"
    demande.save()
    mail = demande.email
    messages.success(request, "Votre demande a été approuvée avec succès !")
    date_delivrance = datetime.date.today() + datetime.timedelta(weeks=2)
    EmailConfirmation(request, mail, date_delivrance)
    
    return redirect('/receptioniste/templates/demandes')
#     # return render(
#     #     request,
#     #     'app/receptioniste/templates/demandes/index.html',
#     #     {
#     #         'demande': demande
#     #     }
#     # )
    
# rejeter---demande
def RejeterDemande(request,id):
    print("Rejeter")
    assert isinstance(request, HttpRequest)
    demande=Rendez_vous.objects.filter(pk=id).first()
    demande.etat="rejeter"
    demande.save()
    mail = demande.email  # Récupérer l'e-mail à partir de l'objet demande
    Rejeter_mail(request, mail)  # Utiliser la variable mail comme argument
    return redirect('/receptioniste/templates/demandes')
    #    return render(
    #     request,
    #     'app/receptioniste/templates/demandes/index.html',
    #     {
    #         'demande':demande
    #     }
    # )


def getEdition(request):
    exetat_id = request.GET.get('exetat_id')
    exetats = Exetat.objects.filter(exetat_id = exetat_id).order_by('annee')
    return render(
        request,
        'app/receptioniste/templates/demandes/getEdition.html',
        {
            'exetats':exetats
        }
    ) 


    

