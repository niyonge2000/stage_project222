from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from app.models import Province,Code_ecole

GENDER = (
    ('masculin', 'Masculin'),
    ('feminin', 'Feminin')
)

TYPE_DOCUMENTS = (
    ('attestation de réussite', 'Attestation de réussite'),
    ('relèvé des points', 'Relèvé des points'),
    ('attestation de participation au concours National', 'Attestation de participation au concours National'),
    ('attestation de participation à l_examen d_etat', 'Attestation de participation à l_examen d_etat')
)
etat = (
    ('approuver', 'Approuver'),
    ('rejeter', 'Rejeter'),
    ('attente', 'Attente')
)

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def edition_year(value):
    current_year = date.today().year
    if value > current_year:
        raise ValidationError(_('L\'année ne peut pas être supérieure à %(current_year)s.'), params={'current_year': current_year})

class Rendez_vous(models.Model):
    nom = models.CharField("Nom", max_length=20)
    prenom = models.CharField("Prenom", max_length=20)
    email = models.EmailField("Email", max_length=100)
    gender = models.CharField("Genre", max_length=10, choices=GENDER)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, default=000)
    code_ecole = models.ForeignKey(Code_ecole, on_delete=models.CASCADE, default=000)
    code_participation = models.PositiveIntegerField("Code_participation")
    type_documents = models.CharField("Type de document", max_length=50, choices=TYPE_DOCUMENTS)
    annee =  models.IntegerField("Edition", validators=[edition_year])
    date_demande = models.DateField("Date de demande", auto_now_add=True)
    date_delivrance = models.DateField("Date de delivrance",null=True, blank=True)
    etat = models.CharField(choices=etat,max_length=20,default='attente',null=True,blank=True)
    recuperer = models.BooleanField(null=True,blank=True,max_length=20,default=True)
    
    
    def __str__(self) -> str:
        return self.nom+" "+self.prenom+" "+self.type_documents+" "+self.etat+" "+self.recuperer
    
    
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['nom', 'prenom', 'code_ecole', 'code_participation','type_documents', 'edition'],
    #             name = 'unique.rendez_vous'
    #         )
    #     ]
    