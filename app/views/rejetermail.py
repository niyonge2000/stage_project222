from django.http import HttpResponse
from django.conf import settings
from datetime import datetime
from django.core.mail import send_mail
from django.core.mail import EmailMessage


from app.models import Rendez_vous

def Rejeter_mail (request, email):
    # dates = Rendez_vous.objects.filter(email = mail).values('date_delivrance')
    # for i in range(0,len(dates)):
    #     date_delivrance = list(dates[i].values())[0]
   send_mail(
        subject="Votre demande de document a été rejetée",
        from_email=None,
        message='Votre demande a été rejetée. Veuillez entrer les informations correctes.',
        recipient_list=[email],
        fail_silently=False
    )
