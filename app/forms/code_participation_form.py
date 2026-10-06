from django.forms import ModelForm
from app.models import Code_participation


class Code_participationForm(ModelForm):
    class Meta:
        model = Code_participation
        fields = '__all__'