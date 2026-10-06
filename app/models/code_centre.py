from django.db import models
from app.models import Province

class Code_centre(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    nom = models.CharField("Nom", max_length=20, unique=True)
    code_centre = models.PositiveIntegerField("Code centre")
        
        
    def __str__(self) -> str:
            return self.nom+" "+str (self.code_centre)
        