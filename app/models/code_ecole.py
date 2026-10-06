from django.db import models
from app.models import Code_centre

class Code_ecole(models.Model):
    code_centre = models.ForeignKey(Code_centre, on_delete=models.CASCADE)
    ecole = models.CharField("Ecole", max_length=20, unique=True)
        
        
    def __str__(self) -> str:
            return str(self.code_centre.nom)+" "+str(self.ecole)
 