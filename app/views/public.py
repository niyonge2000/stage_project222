from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime, timedelta
from app.models import Rendez_vous,Province,Code_centre,Code_ecole,Code_participation
import qrcode


from app.forms import Rendez_vousForm
from .mailsend import EmailConfirmation


def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/public/home/index.html',
        {      
               
        }
    ) 
#formulaire add
def add_formulaire(request):
    if request.method == 'GET' :
        form = Rendez_vousForm()
        provinces = Province.objects.all()
        code_centres = Code_centre.objects.all()
        code_ecoles = Code_ecole.objects.all()
        
    return render(
        request, 
        'app/public/formulaire/formulaire.html',
        {
            'form':form,
            'provinces': provinces,
            'code_centres': code_centres,
            'code_ecoles': code_ecoles
        }
    )
    
# def store(request):
#     if request.method == 'POST':
#         # form = Rendez_vousForm(request.POST)
#         # if form.is_valid():
#         annee = request.POST.get('annee')
#           # nom = form['nom'].value()
#             # prenom = form['prenom'].value()
#             # email = form['email'].value()
#             # gender = form['gender'].value()
#             # code_ecole = form['code_ecole'].value()
#             # code_participation = form['code_participation'].value()
#             # type_documents = form['type_documents'].value()
#             # edition = form['edition'].value()
#             # date_delivrance = datetime.now().date() + timedelta(days=14)
#             # etat = form['etat'].value()
#             # rdv=Rendez_vous.objects.create(nom=nom, prenom=prenom, email=email, gender=gender, code_ecole=code_ecole, code_participation=code_participation,type_documents=type_documents,edition=edition, date_delivrance=date_delivrance, etat=etat)
#         return render(request, 'app/public/formulaire/confirmation.html')
#     else:
#         return render(request, 'app/public/formulaire/formulaire.html')
# def store(request):
#     if request.method == 'POST':
#         form = Rendez_vousForm(request.POST)
#         if form.is_valid():
#             # nom = form['nom'].value()
#             # prenom = form['prenom'].value()
#             # email = form['email'].value()
#             # gender = form['gender'].value()
#             # code_ecole = form['code_ecole'].value()
#             # code_participation = form['code_participation'].value()
#             # type_documents = form['type_documents'].value()
#             # edition = form['edition'].value()
#             # date_delivrance = datetime.now().date() + timedelta(days=14)
#             # etat = form['etat'].value()
#             # rdv=Rendez_vous.objects.create(nom=nom, prenom=prenom, email=email, gender=gender, code_ecole=code_ecole, code_participation=code_participation,type_documents=type_documents,edition=edition, date_delivrance=date_delivrance, etat=etat)
#             form.save();
#             return render(
#                 request,
#                 'app/public/formulaire/confirmation.html'
#             )
#         else :
#             form = Rendez_vousForm(request.POST)
#             messages.error(request, form.errors)
#             # return render(request, 'app/public/formulaire/formulaire.html', {'form': form})
#         # return redirect('/public/formulaire')
        


def store(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        province_id = request.POST.get('province')
        province = Province.objects.filter(id=province_id).first()
        code_ecole_id = request.POST.get('code_ecole')
        code_participation = request.POST.get('code_participation')
        type_documents = request.POST.get('type_documents')
        annee = request.POST.get('annee')
        etat=request.POST.get('etat')
        date_demande=request.POST.get('date_demande')
        date_delivrance=request.POST.get('date_delivrance')
        recuperer=request.POST.get('recuperer')

       
        rendez_vous = Rendez_vous(
            nom=nom,
            prenom=prenom,
            email=email,
            gender=gender,
            province=province,
            code_ecole_id=code_ecole_id,
            code_participation=code_participation,
            type_documents=type_documents,
            annee=annee,
            date_demande=date_demande,
            date_delivrance=date_delivrance,
            etat=etat,
            recuperer=recuperer
        )
        rendez_vous.save()
        return render(request, 'app/public/formulaire/confirmation.html')  # Rediriger vers la page de confirmation
    else:
        return render(request, 'app/public/formulaire/formulaire.html')  # Afficher le formulaire s'il s'agit d'une requête GET
  
    
def getCodeCentre(request):
    province_id = request.GET.get('province_id')
    province=Province.objects.filter(id=province_id).first()
    
    print("ndingahaaaaaaaaaaaaaaaa",province_id)
    code_centres = Code_centre.objects.filter(province_id = province).order_by('nom')
    return render(
        request,
        'app/public/formulaire/getCodeCentre.html',
        {
            'code_centres':code_centres
        }
    )
   
def getCodeEcole(request):
    code_centre_id = request.GET.get('code_centre_id')
    code_ecoles = Code_ecole.objects.filter(code_centre_id = code_centre_id).order_by('nom')
    return render(
        request,
        'app/public/formulaire/getCodeEcole.html',
        {
            'code_ecoles':code_ecoles
        }
    ) 
    
def getCodeParticipation(request):
    code_ecole_id = request.GET.get('code_ecole_id')
    code_participations = Code_participation.objects.filter(code_ecole_id = code_ecole_id).order_by('ecole')
    return render(
        request,
        'app/public/formulaire/getCodeParticipation.html',
        {
            'code_participations':code_participations
        }
    ) 
