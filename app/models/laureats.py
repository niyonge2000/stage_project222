from django.db import models
from app.models import Etudiant,Exetat,Code_ecole


class Laureats(models.Model) :
    
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    exetat = models.ForeignKey(Exetat, on_delete=models.CASCADE)
    code_ecole = models.ForeignKey(Code_ecole, on_delete=models.CASCADE)
    note = models.CharField("Point", max_length=10,unique=True)