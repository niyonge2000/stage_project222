from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import Func, IntegerField, Count
from django.db.models.functions import TruncMonth

from app.models import Rendez_vous,Exetat,Code_centre,Code_ecole

# class ExtractYear(Func):
#     function = 'Extract'
#     template = '%(function)s(YEAR FROM %(expressions)s)'
#     output_field = IntegerField()

def index(request):
    assert isinstance(request, HttpRequest)
    annees = Exetat.objects.values('annee')
    demande = Rendez_vous.objects.annotate(month=TruncMonth('date_demande')).values('month').annotate(total_demande=Count('id'))
    
    datas = []
    for month in demande:
        datas.append({
            'm': month['month'].strftime('%m/%Y'),  # formatage de la date au format mm/aaaa
            'a': month['total_demande']
        })
    datas = sorted(datas, key=lambda x: x['m'])
    
    for i in range(0,len(annees)):
        annee = list(annees[i].values())[0]
    annee = Exetat.objects.filter(annee = annee).count()
    rendez_vous= Rendez_vous.objects.all().count()
    return render(
        request,
        'app/receptioniste/home/index.html',
        {
            'rendez_vous': rendez_vous,
            'annee': annee,
            'datas': datas
        }
    )
    

def queryset_to_list(queryset):
    liste=[]
    for i in range(len(queryset)):
        liste.append(list(queryset[i].values())[0])
    return liste

    
def report_filter_demande(request):
    noms = queryset_to_list(Rendez_vous.objects.all().values("nom").distinct())
    prenoms = queryset_to_list(Rendez_vous.objects.all().values("prenom").distinct())
    emails = queryset_to_list(Rendez_vous.objects.all().values("email").distinct())
    genres = queryset_to_list(Rendez_vous.objects.all().values("gender").distinct())
    # code_centres =  queryset_to_list(Rendez_vous.objects.all().values("code_centre").distinct())
    code_participations = queryset_to_list(Rendez_vous.objects.all().values("code_participation").distinct())
    code_ecoles =  queryset_to_list(Rendez_vous.objects.all().values("code_ecole").distinct())
    type_Documents =  queryset_to_list(Rendez_vous.objects.all().values("type_documents").distinct())
    annees =  queryset_to_list(Rendez_vous.objects.all().values("annee").distinct())
    date_demandes =  queryset_to_list(Rendez_vous.objects.all().values("date_demande").distinct())
    etats =  queryset_to_list(Rendez_vous.objects.all().values("etat").distinct())
    # arable_land_area = queryset_to_list(Household.objects.all().values("arable_land_area").distinct())
    # number_cattle = queryset_to_list(Household.objects.all().values("number_cattle").distinct())
    # responsible_name = queryset_to_list(Household.objects.all().values("responsible_name").distinct())
    # responsible_surname = queryset_to_list(Household.objects.all().values("responsible_surname").distinct())
    # responsible_phone = queryset_to_list(Household.objects.all().values("responsible_phone").distinct())
    # census_date = queryset_to_list(Household.objects.all().values("census_date").distinct())
    print("tous les nomsss",  noms)
    return render(
        request, 
        
        'app/receptioniste/reports/report_filter_demande.html',
        {
            'noms': noms,
            'prenoms': prenoms,
            'emails': emails,
            'genres': genres,
            'code_participations': code_participations,
            'code_ecoles': code_ecoles,
            'type_Documents': type_Documents,
            'annees': annees,
            'date_demandes': date_demandes,
            'etats': etats
            # 'arable_land_area': arable_land_area,
            # 'number_cattle': number_cattle,
            # 'responsible_name': responsible_name,
            # 'responsible_surname': responsible_surname,
            # 'responsible_phone': responsible_phone,
            # 'census_date': census_date,
            # 'provinces': provinces,
            # 'communes': communes,
        }
        )
    
def demande_filter_stab(request):
    if request.method == 'POST':
        selected_nom = request.POST.get('nom')
        selected_prenom = request.POST.get('prenom')
        selected_email = request.POST.get('email')
        selected_genre = request.POST.get('genre')
        selected_code_participation = request.POST.get('code_participation')
        selected_code_ecole = request.POST.get('code_ecole')
        selected_type_documents = request.POST.get('type_documents')
        selected_annee = request.POST.get('annee')
        selected_date_demande = request.POST.get('date_demande')
        selected_etat = request.POST.get('etat')
        
        #----Data for Select Field ----#
        noms = queryset_to_list(Rendez_vous.objects.all().values("nom").distinct())
        prenoms = queryset_to_list(Rendez_vous.objects.all().values("prenom").distinct())
        emails = queryset_to_list(Rendez_vous.objects.all().values("email").distinct())
        genres = queryset_to_list(Rendez_vous.objects.all().values("gender").distinct())
        code_participations = queryset_to_list(Rendez_vous.objects.all().values("code_participation").distinct())
        code_ecoles =  queryset_to_list(Rendez_vous.objects.all().values("code_ecole").distinct())
        type_Documents =  queryset_to_list(Rendez_vous.objects.all().values("type_documents").distinct())
        annees =  queryset_to_list(Rendez_vous.objects.all().values("annee").distinct())
        date_demandes =  queryset_to_list(Rendez_vous.objects.all().values("date_demande").distinct())
        etats =  queryset_to_list(Rendez_vous.objects.all().values("etat").distinct())
        #--------Filtering--------------------------------

        demandes = Rendez_vous.objects.all()
        if selected_nom:
            demandes = demandes.filter(nom = selected_nom)

        if selected_prenom:
            demandes = demandes.filter(prenom = selected_prenom)

        if selected_email:
            demandes = demandes.filter(email = selected_email)
            
        if selected_genre:
            demandes = demandes.filter(gender =selected_genre)
 
        if selected_code_participation:
            demandes = demandes.filter(code_participation = selected_code_participation)
            
        if selected_code_ecole:
            demandes = demandes.filter(code_ecole = selected_code_ecole)
            
        if selected_type_documents:
            demandes = demandes.filter(type_documents = selected_type_documents)
            
        if selected_annee:
            demandes = demandes.filter(type_documents = selected_annee)
            
        if selected_date_demande:
            demandes = demandes.filter(date_demandes = selected_date_demande)

        if selected_etat:
            demandes = demandes.filter(etats = selected_etat)

        # totals_feminins = etudiants.filter( genre = "feminin").count()
        # totals_masculins= etudiants.filter( genre = "masculin").count()
        # totals_etudiants=etudiants.count()
        # context ={
        #     'selected_nom':selected_nom,
        #     'selected_prenom':selected_prenom,
        #     'selected_genre':selected_genre,
        #     'selected_année_naissance':selected_année_naissance,
        #     'selected_commune':selected_commune,
            
        #     'noms': noms,
        #     'prenoms': prenoms,
        #     'genres': genres,
        #     'année_naissances': année_naissances,
        #     'communes': communes,
            
        #     'totals_etudiants':totals_etudiants,
        #     'totals_feminins':totals_feminins,
        #     'totals_masculins':totals_masculins,
            
        #     'etudiants':etudiants,
        # }
        context ={
            'noms': selected_nom,
            'prenoms': selected_prenom,
            'emails': selected_email,
            'genres': selected_genre,
            'code_participations': selected_code_participation,
            'code_ecoles': selected_code_ecole,
            'type_Documents': selected_type_documents,
            'annees': selected_annee,
            'date_demandes': selected_date_demande,
            'etats': selected_etat,
            
           
            
            'demandes':demandes,
        }
        return render(request, 'app/receptioniste/reports/demande_filter_stab.html',context)
    return render(request, 'app/receptioniste/reports/report_filter_demande.html')

# def demande_filtered_mtab(request):
#     if request.method =='POST':
#         selected_nom = request.POST.get('nom')
#         selected_prenom = request.POST.get('prenom')
#         selected_email = request.POST.get('email')
#         selected_genre = request.POST.get('genre')
#         selected_code_ecole = request.POST.get('code_ecole')
#         selected_code_participation = request.POST.get('code_participation')
#         selected_type_documents = request.POST.get('type_documents')
#         selected_annee = request.POST.get('annee')
#         selected_date_demande = request.POST.get('date_demande')
#         selected_etat = request.POST.get('etat')
        
#          #--------Filtering--------------------------------

#         demandes = Rendez_vous.objects.all()
#         if selected_nom:
#             demandes = demandes.filter(nom = selected_nom)

#         if selected_prenom:
#             demandes = demandes.filter(prenom = selected_prenom)

#         if selected_email:
#             demandes = demandes.filter(email = selected_email)
            
#         if selected_genre:
#             demandes = demandes.filter(gender =selected_genre)
 
#         if selected_code_ecole:
#             demandes = demandes.filter(code_ecole = selected_code_ecole)
            
#         if selected_code_participation:
#             demandes = demandes.filter(code_participation = selected_code_participation)
            
#         if selected_type_documents:
#             demandes = demandes.filter(type_documents = selected_type_documents)
            
#         if selected_annee:
#             demandes = demandes.filter(type_documents = selected_annee)
            
#         if selected_date_demande:
#             demandes = demandes.filter(date_demandes = selected_date_demande)

#         if selected_etat:
#             demandes = demandes.filter(etats = selected_etat)

#         context ={
#             'noms': selected_nom,
#             'prenoms': selected_prenom,
#             'emails': selected_email,
#             'genres': selected_genre,
#             'code_ecoles': selected_code_ecole,
#             'code_participations': selected_code_participation,
#             'type_Documents': selected_type_documents,
#             'annees': selected_annee,
#             'date_demandes': selected_date_demande,
#             'etats': selected_etat,
            
           
            
#             'demandes':demandes,
#         }
#     return render(request, 'app/receptioniste/reports/demande_filter_stab.html',context)
        

#report pour l'administrateur

