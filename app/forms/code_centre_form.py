from django.forms import ModelForm
from app.models import Code_centre


class Code_centreForm(ModelForm):
    class Meta:
        model = Code_centre
        fields = '__all__'