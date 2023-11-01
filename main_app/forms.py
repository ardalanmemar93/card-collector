from django.forms import ModelForm
from .models import Apraisal

class ApraisalForm(ModelForm):
    class Meta:
        model = Apraisal
        fields = ['date', 'grade']