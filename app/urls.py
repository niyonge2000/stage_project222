from django.urls import path

from app.views import home, admin,public, provinces,communes,laureates,code_participations,zones,code_centres,code_ecoles,utilisateurs,exetats,cours,sections,cours_sections,etudiants,laureats,demandes, organisateur, agent_de_saisie, receptioniste, qrcode

urlpatterns = [
    path('home/', home.index, name='home'),
    
    #Admin
    path('', admin.index, name='admin_home'),
    #public
    path('public/home/', public.index, name='public_home'),
    
    # path('public/formulaire/', public.formulaire, name='public_formulaire'),
    path('public/formulaire/', public.add_formulaire, name='public_add_formulaire'),
    path('public/formulaire/store', public.store, name='rendez_vous_store'),
    path('public/formulaire/getCodeCentre', public.getCodeCentre, name='demandes_getCodeCentre'),
    path('public/formulaire/getCodeEcole', public.getCodeEcole, name='demandes_getCodeEcole'),
    path('public/formulaire/getCodeParticipation', public.getCodeParticipation, name='demandes_getCodeParticipation'),
    
    
    path('admin/templates/provinces/', provinces.index, name='provinces_index'),
    path('admin/templates/provinces/add', provinces.add, name='provinces_add'),
    path('admin/templates/provinces/store', provinces.store, name='provinces_store'),
    path('admin/templates/provinces/edit/<int:id>', provinces.edit, name='provinces_edit'),
    path('admin/templates/provinces/update/<int:id>', provinces.update, name='provinces_update'),
    path('admin/templates/provinces/delete/<int:id>', provinces.delete, name='provinces_delete'),
    
    path('admin/templates/communes/', communes.index, name='communes_index'),
    path('admin/templates/communes/add', communes.add, name='communes_add'),
    path('admin/templates/communes/store', communes.store, name='communes_store'),
    path('admin/templates/communes/edit/<int:id>', communes.edit, name='communes_edit'),
    path('admin/templates/communes/update/<int:id>', communes.update, name='communes_update'),
    path('admin/templates/communes/delete/<int:id>', communes.delete, name='communes_delete'),
    
    path('admin/templates/zones/', zones.index, name='zones_index'),
    path('admin/templates/zones/add', zones.add, name='zones_add'),
    path('admin/templates/zones/store', zones.store, name='zones_store'),
    path('admin/templates/zones/edit/<int:id>', zones.edit, name='zones_edit'),
    path('admin/templates/zones/update/<int:id>', zones.update, name='zones_update'),
    path('admin/templates/zones/delete/<int:id>', zones.delete, name='zones_delete'),
    path('admin/templates/zones/getCommunes', zones.getCommunes, name='zones_getCommunes'),
   
  
    path('admin/templates/utilisateurs/', utilisateurs.index, name='utilisateurs_index'),
    path('admin/templates/utilisateurs/add', utilisateurs.add, name='utilisateurs_add'),
    path('admin/templates/utilisateurs/store', utilisateurs.store, name='utilisateurs_store'),
    path('admin/templates/utilisateurs/edit/<int:id>', utilisateurs.edit, name='utilisateurs_edit'),
    path('admin/templates/utilisateurs/update/<int:id>', utilisateurs.update, name='utilisateurs_update'),
    path('admin/templates/utilisateurs/delete/<int:id>', utilisateurs.delete, name='utilisateurs_delete'),
    path('admin/templates/utilisateurs/getCommunes', utilisateurs.getCommunes, name='utilisateurs_getCommunes'),
    path('admin/templates/utilisateurs/getZones', utilisateurs.getZones, name='utilisateurs_getZones'),
    
    path('login/',utilisateurs.user_login, name='user_login'),
    path('logout/', utilisateurs.user_logout, name='user_logout'),

    
    
    #organisateur
    path('organisateur/home/', organisateur.index, name='organisateur_home'),
    
    
    # path('organisateur/repo_laureat/report_filter_laureat/',organisateur.report_filter_laureat,name='report_filter_laureat'),
    # path('organisateur/repo_laureat/laureat_filter_stab/',organisateur.laureat_filter_stab,name='laureat_filter_stab'),
    
        
    path('organisateur/templates/exetats/', exetats.index, name='exetats_index'),
    path('organisateur/templates/exetats/add', exetats.add, name='exetats_add'),
    path('organisateur/templates/exetats/store', exetats.store, name='exetats_store'),
    path('organisateur/templates/exetats/edit/<int:id>', exetats.edit, name='exetats_edit'),
    path('organisateur/templates/exetats/update/<int:id>', exetats.update, name='exetats_update'),
    path('organisateur/templates/exetats/delete/<int:id>', exetats.delete, name='exetats_delete'),
    
    #agent_de_saisie
    path('agent_de_saisie/home/', agent_de_saisie.index, name='agent_de_saisie_home'),
    
     
    path('agent_de_saisie/templates/cours/', cours.index, name='cours_index'),
    path('agent_de_saisie/templates/cours/add', cours.add, name='cours_add'),
    path('agent_de_saisie/templates/cours/store', cours.store, name='cours_store'),
    path('agent_de_saisie/templates/cours/edit/<int:id>', cours.edit, name='cours_edit'),
    path('agent_de_saisie/templates/cours/update/<int:id>', cours.update, name='cours_update'),
    path('agent_de_saisie/templates/cours/delete/<int:id>', cours.delete, name='cours_delete'),
    
    path('agent_de_saisie/templates/sections/', sections.index, name='sections_index'),
    path('agent_de_saisie/templates/sections/add', sections.add, name='sections_add'),
    path('agent_de_saisie/templates/sections/store', sections.store, name='sections_store'),
    path('agent_de_saisie/templates/sections/edit/<int:id>', sections.edit, name='sections_edit'),
    path('agent_de_saisie/templates/sections/update/<int:id>', sections.update, name='sections_update'),
    path('agent_de_saisie/templates/sections/delete/<int:id>', sections.delete, name='sections_delete'),
    
    path('agent_de_saisie/templates/cours_sections/', cours_sections.index, name='cours_sections_index'),
    path('agent_de_saisie/templates/cours_sections/add', cours_sections.add, name='cours_sections_add'),
    path('agent_de_saisie/templates/cours_sections/store', cours_sections.store, name='cours_sections_store'),
    path('agent_de_saisie/templates/cours_sections/edit/<int:id>', cours_sections.edit, name='cours_sections_edit'),
    path('agent_de_saisie/templates/cours_sections/update/<int:id>', cours_sections.update, name='cours_sections_update'),
    path('agent_de_saisie/templates/cours_sections/delete/<int:id>', cours_sections.delete, name='cours_sections_delete'),
    
    path('agent_de_saisie/templates/etudiants/', etudiants.index, name='etudiants_index'),
    path('agent_de_saisie/templates/etudiants/add', etudiants.add, name='etudiants_add'),
    path('agent_de_saisie/templates/etudiants/store', etudiants.store, name='etudiants_store'),
    path('agent_de_saisie/templates/etudiants/edit/<int:id>', etudiants.edit, name='etudiants_edit'),
    path('agent_de_saisie/templates/etudiants/update/<int:id>', etudiants.update, name='etudiants_update'),
    path('agent_de_saisie/templates/etudiants/delete/<int:id>', etudiants.delete, name='etudiants_delete'),
    
    path('agent_de_saisie/templates/laureats/', laureats.index, name='laureats_index'),
    path('agent_de_saisie/templates/laureats/add', laureats.add, name='laureats_add'),
    path('agent_de_saisie/templates/laureats/store', laureats.store, name='laureats_store'),
    path('agent_de_saisie/templates/laureats/edit/<int:id>', laureats.edit, name='laureats_edit'),
    path('agent_de_saisie/templates/laureats/update/<int:id>', laureats.update, name='laureats_update'),
    path('agent_de_saisie/templates/laureats/delete/<int:id>', laureats.delete, name='laureats_delete'),


    path('agent_de_saisie/templates/laureates/', laureates.index, name='laureates_index'),
    path('agent_de_saisie/templates/laureates/add', laureates.add, name='laureates_add'),
    path('agent_de_saisie/templates/laureates/store', laureates.store, name='laureates_store'),
    path('agent_de_saisie/templates/laureates/edit/<int:id>', laureates.edit, name='laureates_edit'),
    path('agent_de_saisie/templates/laureates/update/<int:id>', laureates.update, name='laureates_update'),
    path('agent_de_saisie/templates/laureates/delete/<int:id>', laureates.delete, name='laureates_delete'),


    path('agent_de_saisie/templates/CodeCentre/', code_centres.index, name='code_centres_index'),
    path('agent_de_saisie/templates/CodeCentre/add', code_centres.add, name='code_centres_add'),
    path('agent_de_saisie/templates/CodeCentre/store', code_centres.store, name='code_centres_store'),
    path('agent_de_saisie/templates/CodeCentre/edit/<int:id>', code_centres.edit, name='code_centres_edit'),
    path('agent_de_saisie/templates/CodeCentre/update/<int:id>', code_centres.update, name='code_centres_update'),
    path('agent_de_saisie/templates/CodeCentre/delete/<int:id>', code_centres.delete, name='code_centres_delete'), 
    
    path('agent_de_saisie/templates/CodeEcole/', code_ecoles.index, name='code_ecoles_index'),
    path('agent_de_saisie/templates/CodeEcole/add', code_ecoles.add, name='code_ecoles_add'),
    path('agent_de_saisie/templates/CodeEcole/store', code_ecoles.store, name='code_ecoles_store'),
    path('agent_de_saisie/templates/CodeEcole/edit/<int:id>', code_ecoles.edit, name='code_ecoles_edit'),
    path('agent_de_saisie/templates/CodeEcole/update/<int:id>', code_ecoles.update, name='code_ecoles_update'),
    path('agent_de_saisie/templates/CodeEcole/delete/<int:id>', code_ecoles.delete, name='code_ecoles_delete'),   
    
    
    path('agent_de_saisie/templates/CodeParticipation/', code_participations.index, name='code_participations_index'),
    path('agent_de_saisie/templates/CodeParticipation/add', code_participations.add, name='code_participations_add'),
    path('agent_de_saisie/templates/CodeParticipation/store', code_participations.store, name='code_participations_store'),
    path('agent_de_saisie/templates/CodeParticipation/edit/<int:id>', code_participations.edit, name='code_participations_edit'),
    path('agent_de_saisie/templates/CodeParticipation/update/<int:id>', code_participations.update, name='code_participations_update'),
    path('agent_de_saisie/templates/CodeParticipation/delete/<int:id>', code_participations.delete, name='code_participations_delete'),   
    
    #receptioniste
    path('receptioniste/home/', receptioniste.index, name='receptioniste_home'),
    
    path('receptioniste/templates/demandes/', demandes.index, name='demandes_index'),
    path('receptioniste/templates/demandes/add', demandes.add, name='demandes_add'),
    # path('receptioniste/templates/demandes/store', demandes.store, name='demandes_store'),
    # path('receptioniste/templates/demandes/edit/<int:id>', demandes.edit, name='demandes_edit'),
    path('receptioniste/templates/demandes/approuver<int:id>', demandes.ApprouverDemande, name='demandes_ApprouverDemande'),
    path('receptioniste/templates/demandes/rejeter/<int:id>', demandes.RejeterDemande, name='demandes_RejeterDemande'),
    path('receptioniste/templates/demandes/getEdition', demandes.getEdition, name='demandes_getEdition'),
    
    
    
    #report_receptioniste affiche tous les infos demandé par l'etudiant
    
    path('receptioniste/reports/report_filter_demande/',receptioniste.report_filter_demande,name='report_filter_demande'),
    path('receptioniste/reports/demande_filter_stab/',receptioniste.demande_filter_stab,name='demande_filter_stab'),
    
    #report_admin affiche tous les demandes recu dans un mois
    
    path('admin/reports/report_filter_demande/',admin.report_filter_demande,name='report_filter_demande'),
    path('admin/reports/demande_filter_stab/',admin.demande_filter_stab,name='demande_filter_stab'),
    path('admin/reports/demande_filter_mtab/', admin.demande_filtered_mtab, name='demande_filter_mtab'),
    
]
    
    

