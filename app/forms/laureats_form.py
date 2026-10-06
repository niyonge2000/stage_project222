from django.forms import ModelForm
from app.models import Laureats

class LaureatsForm(ModelForm):
    class Meta:
        model = Laureats
        fields = '__all__'