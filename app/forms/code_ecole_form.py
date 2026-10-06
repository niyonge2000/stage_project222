from django.forms import ModelForm
from app.models import Code_ecole


class Code_ecoleForm(ModelForm):
    class Meta:
        model = Code_ecole
        fields = '__all__'