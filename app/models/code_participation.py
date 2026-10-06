from django.db import models
from app.models import Code_ecole

class Code_participation(models.Model):
    Code_ecole = models.ForeignKey(Code_ecole, on_delete=models.CASCADE)
    code_participation = models.PositiveIntegerField("Code_participation")
        
        
    def __str__(self) -> str:
            return str(self.Code_ecole.ecole)+" "+str(self.code_participation)
 